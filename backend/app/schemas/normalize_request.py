from pydantic import BaseModel


class NormalizeRequest(BaseModel):
    text: str