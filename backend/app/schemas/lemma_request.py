from pydantic import BaseModel


class LemmaRequest(BaseModel):
    text: str | None = None
    words: list[str] | None = None