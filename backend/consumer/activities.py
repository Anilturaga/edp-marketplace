from dataclasses import dataclass, field
from typing import Callable

from temporalio import activity, workflow
import asyncio
from tools import (
    response_schema,
)
import time

@dataclass
class InvocationParams:
    user_id: str
    agents: list[str]
    run_id: str


@dataclass
class LLMState:
    user_id: str = ""
    messages: list[dict] = field(default_factory=list)
    tools: list[dict] = field(default_factory=list)
    agents: list[str] = field(default_factory=list)
    # response_format: dict | None = None


@dataclass
class UserMessageParams:
    message: str
    user_id: str = ""


@dataclass
class AgentMessageParams:
    to_id: str
    name: str
    message: str
    user_id: str = ""


@dataclass
class ScheduleParams:
    time: int
    message: str
    user_id: str = ""


@dataclass
class ModelOutputParams:
    contemplation: str
    colleague_messages: list[dict[str, str]] = field(default_factory=list)
    user_message: str | None = None


@activity.defn
async def llm_setup(params: InvocationParams) -> LLMState:
    sys_msg = f"""You are a dedicated personal banking assistant.

    You are responsible for managing all aspects of your user/operator's banking needs related to purchase requests. This includes handling all communication with bank agents, managing tasks, and scheduling reminders.

    1. Task Management & Communication:
    - Process incoming messages and scheduled reminders without user/operator intervention when possible
    - Create and manage tasks autonomously based on known patterns
    - Schedule reminders and follow-ups automatically using the schedule tool
    - Contact bank agents directly for information you need without user/operator involvement

    2. Communication Rules:
    - Handle all routine tasks independently
    - Only involve your user/operator when:
        * You encounter an unknown situation requiring judgment
        * You need approval for important decisions
        * You've completed a significant task
    - All messages must be through the tool call reponse
    - When you are communicating with bank agents, they know that you are an AI assistant

    3. Agent Interactions:
    - Contact bank agents to send purchase requests and receive payment plans and discount details
    - Rank offers based on the best terms and remove duplicate offers from different banks
    - Only notify user/operator of final results or if you need guidance

    User/Operator ID: {params.user_id}
    """

    messages = [{"role": "system", "content": sys_msg}]

    return LLMState(
        user_id=params.user_id,
        messages=messages,
        tools=[
            # send_user_message(),
            # send_user_colleague_message(),
            response_schema(params.agents)
        ],
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
        messages=params.messages, # type: ignore
        tools=params.tools, # type: ignore
        tool_choice=tool_choice,
    )
    print(f"Initial response: {message.model_dump_json(indent=2)}")
    return message.model_dump()

    assert message.stop_reason == "tool_use"

    tool = next(c for c in message.content if c.type == "tool_use")
    response = await client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=1024,
        messages=[
            user_message,
            {"role": message.role, "content": message.content},
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool.id,
                        "content": [{"type": "text", "text": "The weather is 73f"}],
                    }
                ],
            },
        ],
        tools=tools,
    )
    print(f"\nFinal response: {response.model_dump_json(indent=2)}")
    return completion.model_dump()


# @activity.defn
# async def send_user_message_tool(msg: UserMessageParams) -> str:
#     return "Message sent to user. You will be invoked/notified if/when they respond."


@activity.defn
async def send_message_to_agent_tool(params: AgentMessageParams) -> str:
    # Get client and send signal
    from temporalio.client import Client

    client = await Client.connect("localhost:7233")
    colleague_workflow_handle = client.get_workflow_handle(params.to_id)

    # colleague_workflow_handle = workflow.get_external_workflow_handle(params.to_id)
    await colleague_workflow_handle.signal(
        "colleague_msg_signal",
        {
            "from": params.user_id,
            "name": params.name,
            "message": params.message,
        },
    )
    return (
        "Message sent to colleague. You will be invoked/notified if/when they respond."
    )


@activity.defn
async def schedule_tool(params: ScheduleParams) -> str:
    await asyncio.sleep(params.time)
    # Get client and send signal
    from temporalio.client import Client

    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(params.user_id)
    # workflow_id = workflow.info().workflow_id
    # handle = workflow.get_external_workflow_handle(workflow_id)
    await handle.signal(
        "scheduled_msg_signal",
        f"Message scheduled {params.time} seconds ago: {params.message}",
    )
    return "Reminder set."


@activity.defn
async def no_action_tool() -> str:
    return "Done."
