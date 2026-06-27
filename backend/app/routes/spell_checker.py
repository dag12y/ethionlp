from fastapi import APIRouter
from pydantic import BaseModel
from app.services.spell_checker import SpellChecker
from app.services.spell_checker_v2 import SpellChecker as SpellChecker_V2

router = APIRouter()

class SpellRequest(BaseModel):
    text: str


@router.post("/spellcheck/v1")
def spellcheck(req: SpellRequest):

    words = req.text.split()

    results = []

    for w in words:
        results.append(SpellChecker.suggest(w))

    return {
        "results": results
    }

@router.post("/spellcheck/v2")
def spellcheck(req: SpellRequest):

    words = req.text.split()

    results = []

    for w in words:
        results.append(SpellChecker_V2.suggest(w))

    return {
        "results": results
    }
