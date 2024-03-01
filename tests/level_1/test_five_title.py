import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title, expected",
    [
        ("Harry Potter", "Copy of Harry Potter"),
        ("Lord of the Rings", "Copy of Lord of the Rings"),
        ("Star Wars(2)", "Copy of Star Wars(2)"),
    ],
)
def test__change_copy_item__add_copy_text(title, expected):
    assert change_copy_item(title) == expected


@pytest.mark.parametrize(
    "title, expected",
    [
        ("Copy of Harry Potter (2)", "Copy of Harry Potter (3)"),
        ("Copy of Lord of the Rings (2)", "Copy of Lord of the Rings (3)"),
        ("Copy of Star Wars (2)", "Copy of Star Wars (3)"),
    ],
)
def test__change_copy_item__increase_copy_number(title, expected):
    assert change_copy_item(title) == expected


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected",
    [
        ("Harry Potter", 10, "Harry Potter"),
        ("Lord of the Rings", 10, "Lord of the Rings"),
        ("Star Wars(2)", 10, "Star Wars(2)"),
    ],
)
def test__change_copy_item__max_main_item_title_length_less_than_title_length(
    title, max_main_item_title_length, expected
):
    assert change_copy_item(title, max_main_item_title_length) == expected


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected",
    [
        ("Harry Potter", 50, "Copy of Harry Potter"),
        ("Lord of the Rings", 50, "Copy of Lord of the Rings"),
        ("Star Wars(2)", 50, "Copy of Star Wars(2)"),
    ],
)
def test__change_copy_item__max_main_item_title_length_more_than_title_length(
    title, max_main_item_title_length, expected
):
    assert change_copy_item(title, max_main_item_title_length) == expected
