import json
from pathlib import Path

BASE = Path(__file__).parent
FEEDBACK_FILE = BASE / "feedback.json"


def save_feedback(response_id, rating, topic=None):
    data = []
    if FEEDBACK_FILE.exists():
        data = json.loads(FEEDBACK_FILE.read_text())

    data.append({
        "response_id": response_id,
        "rating": rating,
        "topic": topic,
    })

    FEEDBACK_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    return {"status": "saved"}


def get_feedback():
    if not FEEDBACK_FILE.exists():
        return []
    return json.loads(FEEDBACK_FILE.read_text())
