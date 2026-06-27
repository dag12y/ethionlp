import re

def normalize(text: str) -> str:
    # remove punctuation / numbers / weird symbols
    text = re.sub(r"[^\u1200-\u137F\s]", "", text)

    # collapse repeated spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text