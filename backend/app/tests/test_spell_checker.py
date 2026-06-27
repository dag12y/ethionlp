import unittest

from app.routes.spell_checker import SpellRequest, spellcheck_v1, spellcheck_v2, spellcheck_v3
from app.services.spell_checker_ml import SpellCheckerML, frequency_bonus, score


class TestSpellCheckerRoutes(unittest.TestCase):
    def test_spellcheck_v1_returns_expected_top_suggestion(self):
        response = spellcheck_v1(SpellRequest(text="እሄዳሉ"))

        self.assertIn("results", response)
        self.assertEqual(len(response["results"]), 1)

        item = response["results"][0]
        self.assertEqual(item["input"], "እሄዳሉ")
        self.assertTrue(item["suggestions"])
        self.assertEqual(item["suggestions"][0]["word"], "እሄዳለሁ")

    def test_spellcheck_v2_returns_expected_top_suggestion(self):
        response = spellcheck_v2(SpellRequest(text="እሄዳሉ"))

        self.assertIn("results", response)
        self.assertEqual(len(response["results"]), 1)

        item = response["results"][0]
        self.assertEqual(item["input"], "እሄዳሉ")
        self.assertTrue(item["suggestions"])
        self.assertEqual(item["suggestions"][0]["word"], "እሄዳለሁ")

    def test_spellcheck_v3_uses_ml_scoring_and_common_word_bonus(self):
        response = spellcheck_v3(SpellRequest(text="እሄዳሉ"))

        self.assertIn("results", response)
        self.assertEqual(len(response["results"]), 1)

        item = response["results"][0]
        self.assertEqual(item["input"], "እሄዳሉ")
        self.assertTrue(item["suggestions"])
        self.assertEqual(item["suggestions"][0]["word"], "እሄዳለሁ")

    def test_ml_scoring_prefers_common_words(self):
        self.assertGreater(frequency_bonus("ሰላም"), frequency_bonus("ስራ"))
        self.assertLess(score("ሰላም", "ሰላም"), score("ሰላም", "ትምህርት"))

    def test_ml_suggest_returns_ranked_results(self):
        response = SpellCheckerML.suggest("ሰላም", candidates=["ሰላም", "ስራ"], limit=2)

        self.assertEqual(response["input"], "ሰላም")
        self.assertEqual(response["suggestions"][0]["word"], "ሰላም")
        self.assertGreaterEqual(response["suggestions"][0]["frequency"], response["suggestions"][1]["frequency"])


if __name__ == "__main__":
    unittest.main()