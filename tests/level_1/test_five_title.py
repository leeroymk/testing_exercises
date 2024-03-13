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
    "title",
    [
        ("Harry Potter"),
        ("Lord of the Rings"),
        ("Star Wars(2)"),
    ],
)
def test__change_copy_item__max_main_item_title_length_less_than_title_length_title_no_change(
    title,
):
    assert change_copy_item(title, max_main_item_title_length=10) == title


@pytest.mark.parametrize(
    "title, expected",
    [
        ("Harry Potter", "Copy of Harry Potter"),
        ("Lord of the Rings", "Copy of Lord of the Rings"),
        ("Star Wars(2)", "Copy of Star Wars(2)"),
    ],
)
def test__change_copy_item__max_main_item_title_length_more_than_title_length_title_changed(
    title,
    expected,
    max_main_item_title_length=50,
):
    assert change_copy_item(title, max_main_item_title_length) == expected
