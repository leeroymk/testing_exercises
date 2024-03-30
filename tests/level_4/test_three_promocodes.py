import pytest
from functions.level_4.three_promocodes import generate_promocode


@pytest.mark.parametrize("promocode_len", [-1, -10, -100])
def test__generate_promocode__no_promocode_if_promocode_len_is_negative(promocode_len):
    assert len(generate_promocode(promocode_len)) == 0


@pytest.mark.parametrize("promocode_len", [1, 10, 100])
def test__generate_promocode__return_promocode(promocode_len):
    assert len(generate_promocode(promocode_len)) == promocode_len


def test__generate_promocode__promocode_len_is_8_if_no_argument():
    assert len(generate_promocode()) == 8


def test__generate_promocode__no_promocode_if_promocode_len_is_0():
    assert len(generate_promocode(0)) == 0


def test__generate_promocode__only_uppercase_letters():
    assert (generate_promocode(500)).isupper()


def test__generate_promocode__only_letters():
    assert (generate_promocode(500)).isalpha()


def test__generate_promocode__return_str():
    assert isinstance(generate_promocode(10), str)
