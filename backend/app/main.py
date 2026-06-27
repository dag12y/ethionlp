from fastapi import FastAPI
from app.routes.tokenizer import router

app = FastAPI()

app.include_router(router)