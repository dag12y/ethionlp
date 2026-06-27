from fastapi import FastAPI
from app.routes.tokenizer import router as tokenizerRouter
from app.routes.transliteration import router as transliterationRouter
from app.routes.spell_checker import router as spell_router


app = FastAPI()

app.include_router(tokenizerRouter)
app.include_router(transliterationRouter)
app.include_router(spell_router)