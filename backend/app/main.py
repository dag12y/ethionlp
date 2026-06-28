from fastapi import FastAPI
from app.routes.tokenizer import router as tokenizerRouter
from app.routes.transliteration import router as transliterationRouter
from app.routes.spell_checker import router as spell_router
from app.routes.normalizer import router as normalizerRouter
from app.routes.lemmatize import router as lemmatizeRouter
from app.routes.ai import router as aiRouter


app = FastAPI()

app.include_router(tokenizerRouter)
app.include_router(transliterationRouter)
app.include_router(spell_router)
app.include_router(normalizerRouter)
app.include_router(lemmatizeRouter)
app.include_router(aiRouter)