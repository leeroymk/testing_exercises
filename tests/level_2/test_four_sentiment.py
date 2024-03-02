import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.fixture
def good_words():
    return {"good", "nice", "beautiful"}


@pytest.fixture
def bad_words():
    return {"bad", "awful", "terrible"}


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world!", None),
        ("BAD GOOD", None),
        ("once upon a time one poor guy wants to be an it engineer", None),
    ],
)
def test__check_tweet_sentiment__bad_and_good_words_are_equal_return_None(
    text, good_words, bad_words, expected
):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("That was perfectly good", "GOOD"),
        ("You're not good enough", "GOOD"),
    ],
)
def test__check_tweet_sentiment__more_good_words_return_GOOD(
    text, good_words, bad_words, expected
):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Very bad music!", "BAD"),
        ("Bad boy", "BAD"),
    ],
)
def test__check_tweet_sentiment__more_bad_words_return_BAD(
    text, good_words, bad_words, expected
):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected
