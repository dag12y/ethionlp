import unittest

from app.routes.lemmatize import lemmatize
from app.schemas.lemma_request import LemmaRequest


class TestLemmatize(unittest.TestCase):
    def test_lemmatize_returns_batch_output(self):
        response = lemmatize(LemmaRequest(words=["እኔ", "እሄዳለሁ", "ወደ", "ቤት"]))

        self.assertEqual(response["original"], ["እኔ", "እሄዳለሁ", "ወደ", "ቤት"])
        self.assertEqual(response["lemmas"], ["እኔ", "ሄደ", "ወደ", "ቤት"])

    def test_lemmatize_keeps_unknown_words(self):
        response = lemmatize(LemmaRequest(words=["ያልታወቀ"]))

        self.assertEqual(response["original"], ["ያልታወቀ"])
        self.assertEqual(response["lemmas"], ["ያልታወቀ"])

    def test_lemmatize_accepts_sentence_text(self):
        response = lemmatize(LemmaRequest(text="እኔ እሄዳለሁ ወደ ቤት"))

        self.assertEqual(response["original"], ["እኔ", "እሄዳለሁ", "ወደ", "ቤት"])
        self.assertEqual(response["lemmas"], ["እኔ", "ሄደ", "ወደ", "ቤት"])


if __name__ == "__main__":
    unittest.main()