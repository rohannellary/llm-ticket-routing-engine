from app.router import route_ticket

def test_high_priority():
    assert route_ticket("billing", "high") == "priority_support_team"

def test_category_routing():
    assert route_ticket("technical", "low") == "engineering_team"