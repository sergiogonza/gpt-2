from fastapi import APIRouter
from pydantic import BaseModel

from assistant.memory.feedback_engine import save_feedback

router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str


class FeedbackRequest(BaseModel):
    response_id: str
    rating: str
    topic: str | None = None


@router.post('/chat')
def chat(request: ChatRequest):
    return {
        "prompt": request.prompt,
        "response": "Pipeline GPT-2 + RAG pendiente de conexión final"
    }


@router.post('/feedback')
def feedback(request: FeedbackRequest):
    return save_feedback(
        request.response_id,
        request.rating,
        request.topic
    )
