from fastapi import APIRouter

from app.schemas.normalize_request import NormalizeRequest
from app.services.normalizer import Normalizer

router = APIRouter()


@router.post("/normalize")
def normalize_text(request: NormalizeRequest):

    result = Normalizer.normalize(request.text)

    return {
        "original": request.text,
        "normalized": result
    }