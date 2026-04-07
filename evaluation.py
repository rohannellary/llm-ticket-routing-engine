from app.llm import classify_ticket

dataset = [
    {"text": "Payment failed but money deducted", "category": "billing"},
    {"text": "App crashes when I open it", "category": "technical"},
    {"text": "I want to change my password", "category": "account"},
    {"text": "Just asking about features", "category": "general"}
]

def evaluate():
    correct = 0

    for item in dataset:
        pred = classify_ticket(item["text"])

        if pred["category"] == item["category"]:
            correct += 1

    accuracy = correct / len(dataset)
    print(f"Accuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    evaluate()