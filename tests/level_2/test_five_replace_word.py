import pytest

from functions.level_2.five_replace_word import replace_word


def test__replace_word__replace_from_in_text_return_valid_text():
    assert (
        replace_word("some words to replace", "some", "any") == "any words to replace"
    )


def test__replace_word__replace_from_not_in_text_return_old_text():
    assert (
        replace_word("some words to replace", "bad", "any") == "some words to replace"
    )


@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected",
    [
        ("Some words to replace", "some", "any", "any words to replace"),
        ("SOme words to replace", "some", "any", "any words to replace"),
        ("SOMe words to replace", "some", "any", "any words to replace"),
    ],
)
def test__replace_word__ignore_case_return_valid_text(
    text, replace_from, replace_to, expected
):
    assert replace_word(text, replace_from, replace_to) == expected
