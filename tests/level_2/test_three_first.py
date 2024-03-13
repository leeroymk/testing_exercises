import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "default",
    [
        99,
        None,
        "NOT_SET",
    ],
)
def test__first__items_not_empty_any_default_return_first_number(default):
    assert first([111, 2, 3], default) == 111


def test__first__items_empty_default_is_not_set_raise_attribute_error():
    with pytest.raises(AttributeError):
        first(items=[], default="NOT_SET")


@pytest.mark.parametrize(
    "default",
    [1, 2, 0],
)
def test__first__items_empty_default_is_int_return_default(default):
    assert first([], default) == default


def test__first__items_empty_default_is_none_return_none():
    assert first(items=[], default=None) is None
