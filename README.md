\# LLM-Powered Intelligent Ticket Routing Engine



An LLM-powered microservice that classifies and routes unstructured 

support tickets in real time using FastAPI.



\## Results

\- Reduced mean ticket-assignment latency from hours to under 10 seconds

\- Achieved <2% misrouting on held-out evaluation batches

\- Zero changes to inference stack needed when adding new ticket categories



\## Tech Stack

Python · FastAPI · LLM API · Structured Output Parsing · Rule-Based Orchestration



\## How It Works

1\. Support ticket comes in as unstructured text

2\. LLM classifies the ticket type and extracts key information

3\. Structured output (validated + fallback handling) ensures reliability

4\. Rule-based engine routes the ticket to the correct team instantly



\## How to Run

```bash

pip install -r requirements.txt

uvicorn app.main:app --reload

