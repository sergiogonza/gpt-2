from fastapi import FastAPI
from pydantic import BaseModel

from rag.faiss.search import search_documents

app = FastAPI(title="FAISS RAG Bridge API")


class Query(BaseModel):
    query: str
    top_k: int = 5


@app.get("/")
def status():
    return {
        "status": "online",
        "engine": "faiss-rag-bridge"
    }


@app.post("/search")
def search(data: Query):
    results = search_documents(data.query, data.top_k)

    return {
        "query": data.query,
        "results": results,
        "engine": "faiss"
    }
