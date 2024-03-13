import pytest

from functions.level_1.one_gender import genderalize


def test__genderalize__return_male_verb_for_male_gender():
    assert genderalize("verb_male", "verb_female", "male") == "verb_male"


@pytest.mark.parametrize(
    "gender",
    ["female", "not_male", "unknown"],
)
def test__genderalize__return_female_verb_for_not_male_gender(gender):
    assert genderalize("verb_male", "verb_female", gender) == "verb_female"
