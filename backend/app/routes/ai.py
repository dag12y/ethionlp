from fastapi import APIRouter

from app.schemas.ai_request import AIRequest
from app.services.ai_suggestion import improve_text

router = APIRouter()

@router.post("/")
def suggest(request: AIRequest):

    corrected = improve_text(request.text)

    return {
        "original": request.text,
        "suggestion": corrected
    }