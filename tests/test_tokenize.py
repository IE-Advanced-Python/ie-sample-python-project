import pytest

from ie_nlp_utils import tokenize


def test_tokenize_returns_expected_list():
    sentence = "This is a sentence"
    expected_tokens = ["This", "is", "a", "sentence"]

    tokens = tokenize(sentence)

    assert tokens == expected_tokens


@pytest.mark.parametrize("sentence", [
    "THIS IS A SENTENCE",
    "THIS IS A sentence",
    "THIS is a SENTENCE"
])
def test_tokenize_returns_lowercase_tokens(sentence):
    expected_tokens = ["this", "is", "a", "sentence"]

    tokens = tokenize(sentence, lower=True)

    assert tokens == expected_tokens



@pytest.mark.parametrize("sentence, expected_tokens", [
    ("THIS IS A SENTENCE", ["this", "is", "a", "sentence"]),
    ("ANOTHER SENTENCE", ["another", "sentence"]),
])
def test_tokenize_returns_lowercase_tokens_different_sentences(
    sentence,
    expected_tokens,
):
    tokens = tokenize(sentence, lower=True)

    assert tokens == expected_tokens
