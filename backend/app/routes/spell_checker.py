from fastapi import APIRouter
from pydantic import BaseModel
from app.services.spell_checker import SpellChecker

router = APIRouter()

class SpellRequest(BaseModel):
    text: str


@router.post("/spellcheck")
def spellcheck(req: SpellRequest):

    words = req.text.split()

    results = []

    for w in words:
        results.append(SpellChecker.suggest(w))

    return {
        "results": results
    }