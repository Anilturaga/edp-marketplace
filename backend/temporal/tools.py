def response_schema(enums: list[str]) -> dict:
    return {
            "name": "response",
            "description": "Message or response to either your operator or agents of other operators or schedule a reminder for yourself.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "thinking": {
                        "type": "string",
                        "description": "Think out loud if and what action to take next. Can be empty if no thinking is needed.",
                    },
                    "agent_messages": {
                        "type": "array",
                        "description": "Messages to send to agents of other operators. Array can be empty if no messages are to be sent to agents.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "to_id": {
                                    "type": "string",
                                    "description": "user id of the agent.",
                                    "enum": enums,
                                },
                                "message": {
                                    "type": "string",
                                    "description": "The message to send to the agent.",
                                },
                            },
                            "required": ["to_id", "message"],
                            "additionalProperties": False,
                        },
                    },
                    "operator_message": {
                        "type": "string",
                        "description": "Message to send to operator. Can be null if no message is to be sent to operator.",
                    },
                    "schedule_reminder": {
                        "type": "object",
                        "description": "Schedule yourself reminders to follow up on tasks or messages. The reminder will be sent to you at the specified time.",
                        "properties": {
                            "time": {
                                "type": "integer",
                                "description": "The time to schedule the reminder in seconds",
                            },
                            "message": {
                                "type": "string",
                                "description": "Detailed description of the reminder so that you know what to do when you receive it.",
                            },
                        },
                        "required": ["time", "message"],
                    },
                },
            },
    }

if __name__ == "__main__":
    # Define some default enums
    default_enums = ["agent1", "agent2", "agent3"]

    # Call the response_schema function with the default enums
    schema = response_schema(default_enums)

    # Print the schema to see the current enums
    print("Current schema enums:", schema["input_schema"]["properties"]["agent_messages"]["items"]["properties"]["to_id"]["enum"])

    # Edit the enums in the schema
    new_enums = ["agent4", "agent5", "agent6"]
    schema["input_schema"]["properties"]["agent_messages"]["items"]["properties"]["to_id"]["enum"] = new_enums

    # Print the updated schema to verify the changes
    print("Updated schema enums:", schema["input_schema"]["properties"]["agent_messages"]["items"]["properties"]["to_id"]["enum"])