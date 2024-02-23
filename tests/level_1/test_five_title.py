import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title, expected_result",
    [
        ("Harry Potter", "Copy of Harry Potter"),
        ("Lord of the Rings", "Copy of Lord of the Rings"),
        ("Star Wars(2)", "Copy of Star Wars(2)"),
    ],
)
def test_add_copy_text(title, expected_result):
    result = change_copy_item(title)
    assert result == expected_result


@pytest.mark.parametrize(
    "title, expected_result",
    [
        ("Copy of Harry Potter (2)", "Copy of Harry Potter (3)"),
        ("Copy of Lord of the Rings (2)", "Copy of Lord of the Rings (3)"),
        ("Copy of Star Wars (2)", "Copy of Star Wars (3)"),
    ],
)
def test_increase_copy_number(title, expected_result):
    result = change_copy_item(title)
    assert result == expected_result


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected_result",
    [
        ("Harry Potter", 10, "Harry Potter"),
        ("Lord of the Rings", 10, "Lord of the Rings"),
        ("Star Wars(2)", 10, "Star Wars(2)"),
    ],
)
def test_max_main_item_title_length(title, max_main_item_title_length, expected_result):
    result = change_copy_item(title, max_main_item_title_length)
    assert result == expected_result


@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected_error",
    [
        (None, 10, AttributeError),
        ('Harry Potter', None, TypeError),
    ],
)
@pytest.mark.xfail
def test_errors(title, max_main_item_title_length, expected_error):
    with pytest.raises(expected_error):
        change_copy_item(title, max_main_item_title_length)
