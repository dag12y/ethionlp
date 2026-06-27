from fastapi import APIRouter

from app.schemas.lemma_request import LemmaRequest
from app.schemas.lemma_response import LemmaBatchResponse
from app.services.lemmatizer import Lemmatizer

router = APIRouter()

@router.post("/lemmatize", response_model=LemmaBatchResponse)
def lemmatize(request: LemmaRequest):

    if request.words is not None:
        result = Lemmatizer.lemmatize_many(request.words)
    else:
        result = Lemmatizer.lemmatize_text(request.text or "")

    return {
        "original": result["original"],
        "lemmas": result["lemmas"]
    }