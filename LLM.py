from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME
import logging
import time
import json

client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def classify_ticket(text: str):
    prompt = f"""
You are a support ticket classifier.

Return ONLY JSON in this format:
{{
  "category": "<billing|technical|account|general>",
  "priority": "<low|medium|high>"
}}

Ticket:
{text}
"""

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )

            output = response.choices[0].message.content

            # parse + validate
            data = json.loads(output)

            return {
                "category": data.get("category", "general"),
                "priority": data.get("priority", "low")
            }

        except Exception as e:
            logger.error(f"LLM error: {e}")
            time.sleep(1)

    return {
        "category": "general",
        "priority": "low"
    }