import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected",
    [
        ("verb_male", "verb_female", "male", "verb_male"),
    ],
)
def test__genderalize__male_gender(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected",
    [
        ("verb_male", "verb_female", "not_male", "verb_female"),
    ],
)
def test__genderalize__not_male_gender(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected
