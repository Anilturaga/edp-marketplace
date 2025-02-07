from temporalio import workflow
import copy
import asyncio
import json
from temporalio.common import RetryPolicy
from datetime import timedelta
from temporalio.common import datetime


with workflow.unsafe.imports_passed_through():
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
class ConsumerWorkflow:
    @workflow.init
    def __init__(self, params: InvocationParams) -> None:
        self.user_id = params.user_id
        self.user_msg = None
        self.agent_msg_queue = []
        self.scheduled_msg_queue = []
        self.llm_state = LLMState()
        self.tool_activity_mapping = {
            "schedule_reminder": (schedule_tool, ScheduleParams),
            "agent_message" : (send_message_to_agent_tool, AgentMessageParams),
            # "no_action": (no_action_tool, None),
        }
        # self.communication_mapping = {
        #     # "send_user_message": (send_user_message_tool, UserMessageParams),
        #     "send_user_colleague_message": (
        #         send_message_to_agent_tool,
        #         AgentMessageParams,
        #     ),
        # }

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
                or self.user_msg
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
                    "name": clg_msg["name"],
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
            for each_tool_call in message["content"]:
                if each_tool_call["type"] == "tool_use":
                    each_tool_call["id"]
                    each_tool_call["name"]
                    each_tool_call["input"]


            message.stop_reason == "tool_use"
            if completion["stop_reason"] == "tool_use":
                    


                # completion = ChatCompletion(**completion)
                # Get all tool calls
                tool_calls = (
                    completion.choices[0].message.tool_calls
                    if completion.choices[0].message.tool_calls
                    else []
                )

                # Update state with tool calls
                self.llm_state.messages.append(
                    {
                        "role": "assistant",
                        "content": completion.choices[0].message.content,
                        "tool_calls": (
                            [each.model_dump() for each in tool_calls]
                            if len(tool_calls) > 0
                            else None
                        ),
                    }
                )

                if tool_calls:
                    # Execute all tool activities sequentially
                    tool_results = []
                    for tool_call in tool_calls:
                        activity, dataclass = self.tool_activity_mapping[
                            tool_call.function.name
                        ]

                        params = json.loads(tool_call.function.arguments)
                        dataclass_params = dataclass(**params)
                        dataclass_params.user_id = user_id
                        if tool_call.function.name != "schedule_reminder":
                            result = await workflow.execute_activity(
                                activity,
                                dataclass_params,
                                schedule_to_close_timeout=timedelta(hours=2),
                                retry_policy=RetryPolicy(maximum_attempts=1),
                            )
                        else:
                            asyncio.create_task(
                                workflow.execute_activity(
                                    activity,
                                    dataclass_params,
                                    schedule_to_close_timeout=timedelta(hours=2),
                                    retry_policy=RetryPolicy(maximum_attempts=1),
                                )
                            )
                            result = {"message": "Reminder set"}

                        tool_results.append(result)

                    # Update state with all tool responses
                    for tool_call, result in zip(tool_calls, tool_results):
                        self.llm_state.messages.append(
                            {
                                "role": "tool",
                                "content": str(result),
                                "tool_call_id": tool_call.id,
                            }
                        )

                    # # Break loop if any no_action tool was called
                    # if any(
                    #     tool_call.function.name == "no_action"
                    #     for tool_call in tool_calls
                    # ):
                    #     break
                # if completion.choices[0].message.content:
                #     # self.llm_state.messages.append(
                #     #     {
                #     #         "role": "assistant",
                #     #         "content": completion.choices[0].message.content,
                #     #     }
                #     # )
                #     if completion.choices[0].message.content:
                #         parsed_response = json.loads(
                #             completion.choices[0].message.content.encode()
                #         )
                #         dataclass_params = ModelOutputParams(**parsed_response)
                #         if bool(dataclass_params.colleague_messages):
                #             for each in dataclass_params.colleague_messages:
                #                 activity, dataclass = self.communication_mapping[
                #                     "send_user_colleague_message"
                #                 ]

                #                 c_dataclass_params = dataclass(**each)
                #                 c_dataclass_params.user_id = user_id

                #                 res = await workflow.execute_activity(
                #                     send_message_to_agent_tool,
                #                     c_dataclass_params,
                #                     schedule_to_close_timeout=timedelta(hours=2),
                #                     retry_policy=RetryPolicy(maximum_attempts=1),
                #                 )
                        # if dataclass_params.user_message:
                        # activity, dataclass = self.communication_mapping["send_user_message"]

                    break
            continue

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
