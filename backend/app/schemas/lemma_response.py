from pydantic import BaseModel


class LemmaBatchResponse(BaseModel):
    original: list[str]
    lemmas: list[str]