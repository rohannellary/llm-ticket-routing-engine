from pydantic import BaseModel

class TicketRequest(BaseModel):
    ticket_id: str
    text: str

class TicketResponse(BaseModel):
    ticket_id: str
    category: str
    priority: str
    team: str