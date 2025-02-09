from dataclasses import dataclass, field
from typing import Callable
from dotenv import load_dotenv

from temporalio import activity, workflow
from temporalio.client import WorkflowExecutionStatus
import asyncio
from tools import (
    response_schema,
)
import time

from utils.data_mapping import create_mapping
from data.agents_data import agents_data

load_dotenv()


@dataclass
class InvocationParams:
    user_id: str
    run_id: str


@dataclass
class LLMState:
    user_id: str = ""
    persona_type: str = ""
    run_id: str = ""
    system_message: str = ""
    messages: list[dict] = field(default_factory=list)
    tools: list[dict] = field(default_factory=list)
    agents: dict = field(default_factory=dict)
    # response_format: dict | None = None


@dataclass
class UserMessageParams:
    message: str
    user_id: str = ""


@dataclass
class AgentMessageParams:
    to_id: str
    message: str
    user_id: str = ""
    run_id: str = ""
    agents: dict = field(default_factory=dict)


@dataclass
class ScheduleParams:
    time: int
    message: str
    user_id: str = ""
    run_id: str = ""
    persona_type: str = ""


@dataclass
class ModelOutputParams:
    contemplation: str
    colleague_messages: list[dict[str, str]] = field(default_factory=list)
    user_message: str | None = None


@activity.defn
async def llm_setup(params: InvocationParams) -> LLMState:

    mapping = create_mapping(agents_data=agents_data)
    agents = {}
    for each in mapping[params.user_id]["access"]:
        agents[each] = {}
        agents[each]["type"] = mapping[each]["type"]
        agents[each]["about"] = mapping[each]["about"]

    sys_msg = (
        mapping[params.user_id]["system_message"]
        + f"""
Agents you can communicate with:
{agents}
"""
    )

    return LLMState(
        user_id=params.user_id,
        persona_type=mapping[params.user_id]["type"],
        run_id=params.run_id,
        messages=[],
        system_message=sys_msg,
        tools=[
            # send_user_message(),
            # send_user_colleague_message(),
            response_schema(list(agents.keys())),
        ],
        agents=agents,
        # response_format=model_output_schema(),
    )


@activity.defn
async def llm_call(params: LLMState) -> dict:
    from anthropic import Anthropic, AsyncAnthropic
    from anthropic.types import ToolParam, MessageParam, ToolChoiceParam
    import os

    client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # params.tools[0]["input_schema"]["properties"]["agent_messages"]["items"]["properties"]["to_id"]["enum"] = params.agents

    tool_choice: ToolChoiceParam = {
        "name": "response",
        "type": "tool",
        "disable_parallel_tool_use": True,
    }

    message = await client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=8000,
        temperature=0.0,
        system=params.system_message,
        messages=params.messages,  # type: ignore
        tools=params.tools,  # type: ignore
        tool_choice=tool_choice,
    )
    print(f"Initial response: {message.model_dump_json(indent=2)}")
    return message.model_dump()


@activity.defn
async def send_message_to_agent_tool(params: AgentMessageParams) -> str:
    # Get client and send signal
    from temporalio.client import Client

    client = await Client.connect("localhost:7233")
    workflow_id = (
        params.agents[params.to_id]["type"].lower()
        + "-"
        + params.to_id
        + "-"
        + params.run_id
    )
    print("workflow_id", workflow_id)
    try:
        print("**Try checking worflow handle**\n")
        agent_workflow_handle = client.get_workflow_handle(workflow_id)
        workflow_info = await agent_workflow_handle.describe()
        if (
            workflow_info.status == WorkflowExecutionStatus.TERMINATED
            or workflow_info.status == WorkflowExecutionStatus.FAILED
        ):
            print(f"**Worflow terminated/failed**")
            asyncio.create_task(
                client.start_workflow(
                    "Workflow",
                    InvocationParams(user_id=params.to_id, run_id=params.run_id),
                    id=workflow_id,
                    task_queue=params.to_id + "-queue",
                    # id_reuse_policy=4,
                )
            )
            print("**WORKFLOW STARTED")
            await asyncio.sleep(5)
    except Exception as e:
        print(f"**Error getting workflow handle**: {e}")
        asyncio.create_task(
            client.start_workflow(
                "Workflow",
                InvocationParams(user_id=params.to_id, run_id=params.run_id),
                id=workflow_id,
                task_queue=params.to_id + "-queue",
                # id_reuse_policy=4,
            )
        )
        print("**WORKFLOW STARTED")
        await asyncio.sleep(5)
    print("**Signaling workflow**")
    await agent_workflow_handle.signal(
        "agent_msg_signal",
        {
            "from": params.user_id,
            "message": params.message,
        },
    )
    return "Message sent to agent. You will be invoked/notified if/when they respond."


@activity.defn
async def schedule_tool(params: ScheduleParams) -> str:
    await asyncio.sleep(params.time)
    # Get client and send signal
    from temporalio.client import Client

    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(
        params.persona_type.lower() + "-" + params.user_id + "-" + params.run_id
    )
    # workflow_id = workflow.info().workflow_id
    # handle = workflow.get_external_workflow_handle(workflow_id)
    await handle.signal(
        "scheduled_msg_signal",
        f"Message scheduled {params.time} seconds ago: {params.message}",
    )
    return "Reminder task done."
