from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.api import deps
from app.services.rag_service import RAGService

router = APIRouter()
rag_service = RAGService()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
def chat_with_ai(
    request: ChatRequest,
    db: Session = Depends(deps.get_db)
):
    """
    Chat with the AI concierge about restaurants.
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
        
    response_text = rag_service.get_response(db, request.message)
    return ChatResponse(response=response_text)
