from __future__ import annotations

import math

from app.data.word_frequency import WORD_FREQUENCY
from app.utils.levenshtein import levenshtein
from app.utils.normalize import normalize


def prefix_similarity(word: str, candidate: str) -> float:
    if not word or not candidate:
        return 0.0

    matched = 0
    for left, right in zip(word, candidate):
        if left != right:
            break
        matched += 1

    return matched / max(len(word), len(candidate))


def frequency_bonus(word: str) -> float:
    freq = WORD_FREQUENCY.get(word, 0)
    if freq <= 0:
        return 0.0

    # Log scaling keeps common words helpful without overwhelming edit distance.
    return min(3.0, math.log10(freq + 1) * 0.75)


def score(word: str, candidate: str) -> float:
    normalized_word = normalize(word)
    normalized_candidate = normalize(candidate)

    dist = levenshtein(normalized_word, normalized_candidate)
    prefix = prefix_similarity(normalized_word, normalized_candidate)
    freq_bonus = frequency_bonus(normalized_candidate)

    final_score = dist - (prefix * 0.4) - freq_bonus
    return round(final_score, 3)


class SpellCheckerML:
    @staticmethod
    def suggest(word: str, candidates: list[str] | None = None, limit: int = 5):
        normalized_word = normalize(word)
        search_space = candidates if candidates is not None else list(WORD_FREQUENCY.keys())

        results = []
        for candidate in search_space:
            results.append({
                "word": candidate,
                "score": score(normalized_word, candidate),
                "frequency": WORD_FREQUENCY.get(candidate, 0),
            })

        results.sort(key=lambda item: (item["score"], -item["frequency"], item["word"]))

        return {
            "input": normalized_word,
            "suggestions": results[:limit],
        }

