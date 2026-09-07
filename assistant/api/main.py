"""Production HTTP API for RAG + GPT-2 assistant."""

from fastapi import FastAPI
from pydantic import BaseModel

from assistant.api.chat_pipeline import AssistantPipeline

app = FastAPI(title="GPT-2 RAG API")

pipeline = AssistantPipeline()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health():
    return {
        "status": "online",
        "engine": "rag-gpt2-production"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    result = pipeline.chat(request.message)

    return {
        "response": result,
        "model": "gpt2",
        "rag": True
    }
