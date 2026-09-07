from fastapi import FastAPI
from pydantic import BaseModel
from server import assistant_response

app = FastAPI(title="GPT-2 RAG Assistant")

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def health():
    return {"status":"online","engine":"gpt-2-rag"}

@app.post("/api/chat")
def chat(data: ChatRequest):
    return {"answer": assistant_response(data.query)}
