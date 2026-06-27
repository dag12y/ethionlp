import re

from app.data.normalization_map import NORMALIZATION_MAP


class Normalizer:

    @staticmethod
    def normalize(text: str):

        # Character normalization
        normalized = "".join(
            NORMALIZATION_MAP.get(char, char)
            for char in text
        )

        # Remove punctuation
        normalized = re.sub(
            r"[!?,.:;።፣፤፥፦፧፨]+",
            "",
            normalized
        )

        # Remove extra spaces
        normalized = re.sub(
            r"\s+",
            " ",
            normalized
        ).strip()

        return normalized