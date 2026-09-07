from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from pathlib import Path

try:
    from server import assistant_response
except Exception:
    def assistant_response(query):
        return "Backend conectado. Motor GPT-2 pendiente de carga."

app = FastAPI(title="GPT-2 RAG Assistant")

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

class FeedbackRequest(BaseModel):
    query: str
    answer: str
    rating: str

@app.get("/")
def health():
    return {"status":"online","engine":"gpt-2-rag"}

@app.post("/api/chat")
def chat(data: ChatRequest):
    answer = assistant_response(data.query)
    return {
        "answer": answer,
        "sources": [],
        "memory": True
    }

@app.post("/api/feedback")
def feedback(data: FeedbackRequest):
    records = []
    if MEMORY_FILE.exists():
        records = json.loads(MEMORY_FILE.read_text())

    records.append(data.model_dump())
    MEMORY_FILE.write_text(json.dumps(records, indent=2, ensure_ascii=False))

    return {"saved": True}
