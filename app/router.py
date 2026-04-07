def route_ticket(category: str, priority: str) -> str:
    routing_table = {
        "billing": "finance_team",
        "technical": "engineering_team",
        "account": "support_team",
        "general": "customer_success"
    }

    if priority == "high":
        return "priority_support_team"

    return routing_table.get(category, "default_team")