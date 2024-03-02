import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.fixture
def text():
    return "and once again the grey night is the only one I trust"



@pytest.mark.parametrize(
    "replace_from, replace_to, expected", [
        ("again", "snova", "and once snova the grey night is the only one I trust"),
    ]
)
def test__replace_word__replace_from_in_text_return_new_text(
    text, replace_from, replace_to, expected
    ):
    assert replace_word(text, replace_from, replace_to) == expected


@pytest.mark.parametrize(
    "replace_from, replace_to, expected", [
        ("snova", "again", "and once again the grey night is the only one I trust"),
    ]
)
def test__replace_word__replace_from_not_in_text_return_old_text(
    text, replace_from, replace_to, expected
    ):
    assert replace_word(text, replace_from, replace_to) == expected
