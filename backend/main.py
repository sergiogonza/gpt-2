from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from pathlib import Path
from datetime import datetime

try:
    from server import assistant_response
except Exception:
    def assistant_response(query, context=None):
        return "Backend conectado. Motor GPT-2 pendiente de carga.", context or []

app = FastAPI(title="GPT-2 Semantic Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

MEMORY_FILE = Path("memory_feedback.json")

class ChatRequest(BaseModel):
    query: str
    prompt: str | None = None
    rag: bool = True
    memory: bool = True

class FeedbackRequest(BaseModel):
    query: str
    answer: str
    rating: str

@app.get("/")
def health():
    return {"status":"online","engine":"gpt-2-semantic-rag"}

@app.post("/api/chat")
def chat(data: ChatRequest):
    answer, sources = assistant_response(data.query, {
        "rag": data.rag,
        "memory": data.memory,
        "prompt": data.prompt
    })
    return {
        "answer": answer,
        "sources": sources,
        "memory": data.memory,
        "rag": data.rag
    }

@app.post("/api/feedback")
def feedback(data: FeedbackRequest):
    records = []
    if MEMORY_FILE.exists():
        records = json.loads(MEMORY_FILE.read_text())

    item = data.model_dump()
    item["timestamp"] = datetime.utcnow().isoformat()
    records.append(item)

    MEMORY_FILE.write_text(json.dumps(records, indent=2, ensure_ascii=False))
    return {"saved": True}
