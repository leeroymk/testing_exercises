import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text",
    [
        "Hello world!",
        "BAD GOOD",
        "once upon a time one poor guy wants to be an it engineer",
    ],
)
def test__check_tweet_sentiment__bad_and_good_words_are_equal_return_None(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) is None


@pytest.mark.parametrize(
    "text",
    [
        "That was perfectly good",
        "You're not good enough",
    ],
)
def test__check_tweet_sentiment__more_good_words_return_GOOD(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


@pytest.mark.parametrize(
    "text",
    [
        "Very bad music!",
        "Bad boy",
    ],
)
def test__check_tweet_sentiment__more_bad_words_return_BAD(text, good_words, bad_words):
    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"
