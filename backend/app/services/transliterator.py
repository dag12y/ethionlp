from app.data.SERA_Mapping import SERA_MAP



class Transliterator:

    @staticmethod
    def transliterate(text: str, mode: str):

        result = ""

        for char in text:
            result += SERA_MAP.get(char, char)
        if mode == "academic":
            return result
        else:
            return academic_to_friendly(result)

def academic_to_friendly(text):
    replacements = {
        "č̣": "ch",
        "č": "ch",
        "š": "sh",
        "ṣ́": "s",
        "ṣ": "s",
        "ṭ": "t",
        "ḥ": "h",
        "ḫ": "h",
        "ñ": "ny",
        "ž": "zh",
        "ǧ": "j",
        "ä": "e",
        "ē": "e",
        "ə": "",
        "ʼ": "",
        "ʻ": "",
        "ʰ": "",
        "ʷ": "w"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text