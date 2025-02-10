
def create_mapping(agents_data):
    mapping = {}
    
    def format_system_message(persona, agent_type, system_message):
        if agent_type == "Issuer":
            return system_message.format(
                user_id=persona["user_id"],
                payment_plans=persona.get("payment_plans", ""),
                user_details=persona.get("user_details", "")
            )
        elif agent_type == "Merchant":
            return system_message.format(
                user_id=persona["user_id"],
                products_inventory=persona.get("products_inventory", "")
            )
        else:
            return system_message.format(user_id=persona["user_id"])

    for agent_type, data in agents_data.items():
        for persona in data["personas"]:
            user_id = persona["user_id"]
            
            mapping[user_id] = {
                "type": agent_type,
                "about": persona["about"],
                "system_message": format_system_message(
                    persona,
                    agent_type,
                    data["system_message"]
                ),
                "access": persona["access"]
            }
    
    return mapping
