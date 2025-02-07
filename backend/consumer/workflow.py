from temporalio import workflow
import copy
import asyncio
import json
from temporalio.common import RetryPolicy
from datetime import timedelta


with workflow.unsafe.imports_passed_through():
    from temporalio.common import datetime # type: ignore
    from activities import (
        llm_call,
        llm_setup,
        LLMState,
        # send_user_message_tool,
        send_message_to_agent_tool,
        schedule_tool,
        # no_action_tool,
        UserMessageParams,
        AgentMessageParams,
        ScheduleParams,
        ModelOutputParams,
        InvocationParams,
    )
    from openai.types.chat.chat_completion import ChatCompletion
    from jiter import from_json


@workflow.defn
class Workflow:
    @workflow.init
    def __init__(self, params: InvocationParams) -> None:
        self.user_id = params.user_id
        self.user_msg = None
        self.agent_msg_queue = []
        self.scheduled_msg_queue = []
        self.llm_state = LLMState()


    @workflow.run
    async def run(self, params: InvocationParams) -> dict:

        self.llm_state = await workflow.execute_activity(
            llm_setup,
            params,
            schedule_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(maximum_attempts=1),
        )
        while True:
            await workflow.wait_condition( 
                lambda: bool(self.agent_msg_queue)
                or bool(self.user_msg)
                or bool(self.scheduled_msg_queue)
            ) 

            # get time string in yyyy-mm-dd hh:mm:ss format
            time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.user_msg:
                signal_msg = {
                    "from": "user",
                    "current_time": time_str,
                    "message": self.user_msg,
                }
                self.user_msg = None
                self.llm_state.messages.append(
                    {"role": "user", "content": json.dumps(signal_msg, indent=2)}
                )

            elif bool(self.agent_msg_queue):
                clg_msg = self.agent_msg_queue.pop(0)
                signal_msg = {
                    "from": "agent",
                    "agent_id": clg_msg["from"],
                    "current_time": time_str,
                    "message": clg_msg["message"],
                }
                self.llm_state.messages.append(
                    {"role": "user", "content": json.dumps(signal_msg, indent=2)}
                )
            elif bool(self.scheduled_msg_queue):
                sch_msg = self.scheduled_msg_queue.pop(0)
                signal_msg = {
                    "from": "scheduled_reminder",
                    "current_time": time_str,
                    "message": sch_msg,
                }
                self.llm_state.messages.append(
                    {"role": "user", "content": json.dumps(signal_msg, indent=2)}
                )

            message = await workflow.execute_activity(
                llm_call,
                self.llm_state,
                schedule_to_close_timeout=timedelta(seconds=30),
                retry_policy=RetryPolicy(maximum_attempts=1),
            )
            self.llm_state.messages.append(message)

            tool_response_string = ""
            tool_id = None
            for each_tool_call in message["content"]:
                if each_tool_call["type"] == "tool_use":
                    tool_if = each_tool_call["id"]
                    each_tool_call["name"]
                    each_tool_call["input"]
                    thinking = each_tool_call["input"].get("thinking", None)
                    agent_messages = each_tool_call["input"].get("agent_messages", [])
                    operator_message = each_tool_call["input"].get(
                        "operator_message", None
                    )
                    schedule_reminder = each_tool_call["input"].get(
                        "schedule_reminder", None
                    )
                    if thinking:
                        print("Thinking: ", thinking)
                    if agent_messages:
                        for each_agent_message in agent_messages:
                            print("Agent Message: ", each_agent_message)
                            to_id = each_agent_message["to_id"]
                            message = each_agent_message["message"]
                            
                            agent_message_params = AgentMessageParams(
                                to_id=to_id,
                                message=message,
                                user_id=self.user_id,
                                run_id = params.run_id,
                                agents = self.llm_state.agents
                            )

                            result = await workflow.execute_activity(
                                "send_message_to_agent_tool",
                                agent_message_params,
                                schedule_to_close_timeout=timedelta(hours=2),
                                retry_policy=RetryPolicy(maximum_attempts=1),
                            )

                            
                            tool_response_string += result


                    if operator_message:
                        print("Operator Message: ", operator_message)
                        tool_response_string += "Your operator has been notified."

                    if schedule_reminder:
                        #                 self.tool_activity_mapping = {
                        #     "schedule_reminder": (schedule_tool, ScheduleParams),
                        #     "agent_message" : (send_message_to_agent_tool, AgentMessageParams),
                        #     # "no_action": (no_action_tool, None),
                        # }
                        schedule_params = ScheduleParams(
                            time=schedule_reminder["time"],
                            message=schedule_reminder["message"],
                            user_id=self.user_id,
                            run_id = params.run_id
                        )

                        asyncio.create_task(
                            workflow.execute_activity(
                                "schedule_reminder",
                                schedule_params,
                                schedule_to_close_timeout=timedelta(hours=2),
                                retry_policy=RetryPolicy(maximum_attempts=1),
                            )
                        )
                        tool_response_string += "Reminder set."
            self.llm_state.messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_id,
                        "content": [{"type": "text", "text": tool_response_string}],
                    }
                ],
            })                

    @workflow.signal
    def user_msg_signal(self, input: str) -> None:
        # 👉 A Signal handler mutates the Workflow state but cannot return a value.
        self.user_msg = input

    @workflow.signal
    def agent_msg_signal(self, input: dict) -> None:
        # 👉 A Signal handler mutates the Workflow state but cannot return a value.
        self.agent_msg_queue.append(input)

    @workflow.signal
    def scheduled_msg_signal(self, input: str) -> None:
        # 👉 A Signal handler mutates the Workflow state but cannot return a value.
        self.scheduled_msg_queue.append(input)

    @workflow.query
    def get_state(self) -> str:
        print("Querying state", self.llm_state)
        state_dict = {}
        for field in self.llm_state.__dataclass_fields__:
            state_dict[field] = getattr(self.llm_state, field)
        return json.dumps(state_dict, indent=2)
