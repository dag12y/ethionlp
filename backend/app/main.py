from fastapi import FastAPI
from app.routes.tokenizer import router as tokenizerRouter
from app.routes.transliteration import router as transliterationRouter

app = FastAPI()

app.include_router(tokenizerRouter)
app.include_router(transliterationRouter)