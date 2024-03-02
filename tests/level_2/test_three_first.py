import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "items, default, expected",
    [
        ([111, 2, 3], 99, 111),
        ([111, 2, 3], None, 111),
        ([111, 2, 3], "NOT_SET", 111),
    ],
)
def test__first__items_not_empty_return_first_number(items, default, expected):
    assert first(items, default) == expected


@pytest.mark.parametrize(
    "items, default, expected",
    [
        ([], "NOT_SET", AttributeError),
    ],
)
def test__first__items_empty_default_NOT_SET_raise_Attribute_Error(
    items, default, expected
):
    with pytest.raises(expected):
        first(items, default)


@pytest.mark.parametrize(
    "items, default, expected",
    [
        ([], 100, 100),
        ([], 0, 0),
        ([], -100, -100),
    ],
)
def test__first__items_empty_default_int_return_default(items, default, expected):
    assert first(items, default) == expected


@pytest.mark.parametrize(
    "items, default, expected",
    [
        ([], None, None),
    ],
)
def test__first__items_empty_default_None_return_None(items, default, expected):
    assert first(items, default) == expected
