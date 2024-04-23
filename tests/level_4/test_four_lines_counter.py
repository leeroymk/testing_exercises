import pytest

from functions.level_4.four_lines_counter import count_lines_in
from tests.level_4.conftest import remove_temp_file


def test__count_lines_in__return_nont_when_nonexistent_file():
    assert count_lines_in("nonexistent_file.txt") is None


def test__count_lines_in__return_zero_when_empty_file(create_file):
    filepath = "empty_file.txt"
    create_file(filepath, lines=0, comments=0)

    assert count_lines_in(filepath) == 0

    remove_temp_file(filepath)


@pytest.mark.parametrize("comments", [1, 10, 100])
def test__count_lines_in__return_zero_when_file_with_only_comments(create_file, comments):
    filepath = "comments_file.txt"
    create_file(filepath, lines=0, comments=comments)

    assert count_lines_in(filepath) == 0

    remove_temp_file(filepath)


@pytest.mark.parametrize("lines, comments", [(1, 1), (10, 2), (150, 33)])
def test__count_lines_in__return_correct_value_when_file_with_lines_and_comments(
    create_file, lines, comments
):
    filepath = "mixed_file.txt"
    create_file(filepath, lines=lines, comments=comments)

    assert count_lines_in(filepath) == lines

    remove_temp_file(filepath)


@pytest.mark.parametrize("lines", [1, 10, 100])
def test__count_lines_in__return_correct_value_when_file_with_only_lines(create_file, lines):
    filepath = "lines_file.txt"
    create_file(filepath, lines=lines, comments=0)

    assert count_lines_in(filepath) == lines

    remove_temp_file(filepath)
