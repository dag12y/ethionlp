from app.data.amharic_words import AMHARIC_WORDS
from app.utils.levenshtein import levenshtein
from app.utils.normalize import normalize
from app.utils.score import score

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

    