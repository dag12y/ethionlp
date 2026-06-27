from app.data.amharic_words import AMHARIC_WORDS
from app.utils.levenshtein import levenshtein

class SpellChecker:

    @staticmethod
    def suggest(word: str):

        suggestions = []

        for w in AMHARIC_WORDS:
            distance = levenshtein(word, w)

            suggestions.append({
                "word": w,
                "distance": distance
            })

        # sort best matches first
        suggestions.sort(key=lambda x: x["distance"])

        return {
            "input": word,
            "suggestions": suggestions[:3]  # top 3
        }