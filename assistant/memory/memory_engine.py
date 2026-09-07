import json
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent

FILES = {
    "conversations": BASE / "conversations.json",
    "feedback": BASE / "feedback.json",
    "preferences": BASE / "preferences.json",
}

for f in FILES.values():
    if not f.exists():
        f.write_text("[]", encoding="utf-8")


def save_conversation(question, answer, context=None):
    data = json.loads(FILES["conversations"].read_text())
    data.append({
        "time": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "context": context or []
    })
    FILES["conversations"].write_text(json.dumps(data, indent=2), encoding="utf-8")


def save_feedback(answer_id, rating):
    data = json.loads(FILES["feedback"].read_text())
    data.append({"id": answer_id, "rating": rating})
    FILES["feedback"].write_text(json.dumps(data, indent=2), encoding="utf-8")
