# EthioNLP Version 1 Checklist

This checklist separates the current implementation from the remaining work needed to make Version 1 feel complete and documented.

## Done

- FastAPI app entrypoint exists in `backend/app/main.py`
- Tokenizer route is wired through `/analyze`
- Transliteration route is wired through `/transliterate`
- Spell checker v1 route is wired through `/spellcheck/v1`
- Spell checker v2 route is wired through `/spellcheck/v2`
- Request schemas exist for text and transliteration inputs
- Core tokenizer logic exists in `backend/app/services/tokenizer.py`
- Transliteration mapping exists in `backend/app/data/SERA_Mapping.py`
- Spell checker v1 uses Levenshtein distance
- Spell checker v2 uses normalization and weighted scoring
- A tokenization test already exists

## In Progress

- Documentation cleanup so route names match the actual backend
- Aligning README feature summary with the implemented modules
- Expanding tests beyond tokenization

## Missing Or Needs Review

- Response schemas for API outputs are not formalized yet
- Spell checker endpoints return simple Python dicts instead of typed response models
- There is no dedicated test coverage for transliteration
- There is no dedicated test coverage for spell checker v1
- There is no dedicated test coverage for spell checker v2
- The frontend is present, but its API wiring is not confirmed from the backend code alone
- The documentation still describes Version 2, 3, and 4 ideas that are not implemented yet

## Recommended Next Steps

1. Add response schemas for analyze, transliterate, and spell-check endpoints.
2. Add tests for transliteration and both spell-check versions.
3. Decide whether the frontend should consume the current backend routes directly or use a small API adapter layer.
4. Keep `docs/v1.md` focused on what is actually shipped in Version 1.