from fastapi import FastAPI
from pydantic import BaseModel
from model import generate
from rag import retrieve_context

app = FastAPI(title="GPT-2 RAG Assistant")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "GPT-2 RAG API running"}

@app.post("/chat")
def chat(req: ChatRequest):
    context = retrieve_context(req.prompt)
    answer = generate(req.prompt, context)
    return {
        "response": answer,
        "context": context
    }
