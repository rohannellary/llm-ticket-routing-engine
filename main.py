from fastapi import FastAPI
from app.schemas import TicketRequest, TicketResponse
from app.llm import classify_ticket
from app.router import route_ticket
import logging

app = FastAPI(title="LLM Ticket Routing Engine")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/route", response_model=TicketResponse)
async def route_ticket_api(ticket: TicketRequest):
    logger.info(f"Processing ticket {ticket.ticket_id}")

    parsed = classify_ticket(ticket.text)
    team = route_ticket(parsed["category"], parsed["priority"])

    return TicketResponse(
        ticket_id=ticket.ticket_id,
        category=parsed["category"],
        priority=parsed["priority"],
        team=team
    )