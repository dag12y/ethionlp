from app.services.tokenizer import Tokenizer

def test_tokenize():
    text = "እኔ ወደ ቤት እሄዳለሁ።"

    tokens = Tokenizer.tokenize(text)

    assert len(tokens) == 4