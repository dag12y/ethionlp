from fastapi import APIRouter
from app.schemas.text_request import TextRequest
from app.services.tokenizer import Tokenizer

router = APIRouter()

@router.post("/analyze")
def analyze(request: TextRequest):

    tokens = Tokenizer.tokenize(request.text)

    return {
        "tokens": tokens,
        "word_count": Tokenizer.word_count(tokens),
        "sentence_count": Tokenizer.sentence_count(request.text),
        "character_count": Tokenizer.character_count(request.text),
        "unique_words":Tokenizer.unique_words(tokens),
        "word_frequency":Tokenizer.word_frequency(tokens)
    }