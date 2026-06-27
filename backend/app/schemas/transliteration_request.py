from pydantic import BaseModel
from typing import Literal

class TransliterationRequest(BaseModel):
    text: str
    mode: Literal["academic", "friendly"] = "friendly"