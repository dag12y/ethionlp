import re
from app.data.amharic_words import AMHARIC_WORDS
from app.utils.levenshtein import levenshtein

def normalize(text: str) -> str:
    # remove punctuation / numbers / weird symbols
    text = re.sub(r"[^\u1200-\u137F\s]", "", text)

    # collapse repeated spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def score(word: str, candidate: str) -> float:
    dist = levenshtein(word, candidate)

    # base score (lower is better)
    score = dist

    # 1. length penalty (small difference preferred)
    score += abs(len(word) - len(candidate)) * 0.2

    # 2. prefix bonus (VERY important for Amharic)
    prefix_len = 0
    for a, b in zip(word, candidate):
        if a == b:
            prefix_len += 1
        else:
            break

    score -= prefix_len * 0.3

    return score


class SpellChecker:

    @staticmethod
    def suggest(word: str):
        word = normalize(word)

        results = []

        for w in AMHARIC_WORDS:
            s = score(word, w)

            results.append({
                "word": w,
                "score": round(s, 3)
            })

        results.sort(key=lambda x: x["score"])

        return {
            "input": word,
            "suggestions": results[:5]
        }

    