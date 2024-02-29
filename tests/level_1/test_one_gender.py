import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected_result",
    [
        ("verb_male", "verb_female", "male", "verb_male"),
        ("verb_male", "verb_female", "somethingelse", "verb_female"),
    ],
)
def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result


@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected_error",
    [
        (None, None, "male", ValueError),
        ("", "", "male", ValueError),
        (1, 2, "male", TypeError),
        ("verb_male", "verb_female", 1, TypeError),
        ("verb_male", "verb_female", None, TypeError),
    ],
)
@pytest.mark.xfail
def test_errors(verb_male, verb_female, gender, expected_error):
    with pytest.raises(expected_error):
        genderalize(verb_male, verb_female, gender)
