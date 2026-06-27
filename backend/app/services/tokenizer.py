import re
from collections import Counter

class Tokenizer:
    @staticmethod
    def tokenize(text: str):
        text = re.sub(r"[።፣፤፥፦!?.,]", "", text)

        tokens = text.split()

        return tokens

    @staticmethod
    def word_count(tokens):
        return len(tokens)

    @staticmethod
    def sentence_count(text):
        sentences = re.findall(r"[።!?]", text)
        return len(sentences)

    @staticmethod
    def character_count(text):
        return len(text.replace(" ", ""))

    @staticmethod
    def unique_words(tokens):
        return len(set(tokens))
    
    @staticmethod
    def word_frequency(tokens):
        return Counter(tokens)

