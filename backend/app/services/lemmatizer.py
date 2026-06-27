from app.data.lemma_dictionary import LEMMAS

REVERSE_LOOKUP = {}

for lemma, variants in LEMMAS.items():
    for word in variants:
        REVERSE_LOOKUP[word] = lemma


class Lemmatizer:

    @staticmethod
    def lemmatize(word: str):
        lemma = REVERSE_LOOKUP.get(word)

        return {
            "lemma": lemma if lemma is not None else word,
            "found": lemma is not None,
        }

    @staticmethod
    def lemmatize_many(words: list[str]):
        original = []
        lemmas = []

        for word in words:
            result = Lemmatizer.lemmatize(word)
            original.append(word)
            lemmas.append(result["lemma"])

        return {
            "original": original,
            "lemmas": lemmas,
        }

    @staticmethod
    def lemmatize_text(text: str):
        words = [word for word in text.split() if word]
        return Lemmatizer.lemmatize_many(words)