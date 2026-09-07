from fastapi import FastAPI
from pydantic import BaseModel
from model import generate
from rag import retrieve_context

app = FastAPI(title="GPT-2 Semantic RAG Assistant")


class ChatRequest(BaseModel):
    prompt: str
    memory: bool = True
    rag: bool = True


@app.get("/")
def home():
    return {
        "status": "online",
        "engine": "gpt-2-rag",
        "model": "gpt2"
    }


@app.post("/chat")
def chat(req: ChatRequest):
    context = ""

    if req.rag:
        context = retrieve_context(req.prompt)

    answer = generate(
        req.prompt,
        context
    )

    return {
        "response": answer,
        "context": context,
        "rag_enabled": req.rag,
        "memory_enabled": req.memory
    }


def assistant_response(query, options=None):
    options = options or {}

    use_rag = options.get("rag", True)
    context = retrieve_context(query) if use_rag else ""

    answer = generate(
        query,
        context
    )

    return answer, [context] if context else []
