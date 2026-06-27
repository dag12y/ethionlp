from collections.abc import Mapping

from pydantic import BaseModel, Field


class AnalyzeResponse(BaseModel):
    tokens: list[str]
    word_count: int
    sentence_count: int
    character_count: int
    unique_words: int
    word_frequency: Mapping[str, int]


class TransliterationResponse(BaseModel):
    original: str
    mode: str
    transliteration: str


class SpellSuggestionV1(BaseModel):
    word: str
    distance: int


class SpellCheckItemV1(BaseModel):
    input: str
    suggestions: list[SpellSuggestionV1] = Field(default_factory=list)


class SpellCheckResponseV1(BaseModel):
    results: list[SpellCheckItemV1]


class SpellSuggestionV2(BaseModel):
    word: str
    score: float


class SpellCheckItemV2(BaseModel):
    input: str
    suggestions: list[SpellSuggestionV2] = Field(default_factory=list)


class SpellCheckResponseV2(BaseModel):
    results: list[SpellCheckItemV2]