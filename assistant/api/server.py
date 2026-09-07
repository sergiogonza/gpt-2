from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="GPT-2 RAG Assistant")

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {"status": "online", "service": "gpt-2-assistant"}

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "prompt": request.prompt,
        "response": "Assistant pipeline ready. Connect GPT-2 inference and RAG retrieval next."
    }
