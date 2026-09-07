from fastapi import FastAPI
from pydantic import BaseModel
from model import generate

app = FastAPI(title="GPT-2 RAG Assistant")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "GPT-2 RAG API running"}

@app.post("/chat")
def chat(req: ChatRequest):
    return {"response": generate(req.prompt)}
