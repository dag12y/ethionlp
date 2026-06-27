from fastapi import APIRouter
from app.schemas.transliteration_request import TransliterationRequest
from app.services.transliterator import Transliterator

router = APIRouter()

@router.post("/transliterate")
def transliterate(request: TransliterationRequest):

    result = Transliterator.transliterate(
        request.text,
        request.mode
    )

    return {
        "original": request.text,
        "mode": request.mode,
        "transliteration": result
    }