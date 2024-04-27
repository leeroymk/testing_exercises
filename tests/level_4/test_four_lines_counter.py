import pytest

from functions.level_4.four_lines_counter import count_lines_in


def test__count_lines_in__return_nont_when_nonexistent_file():
    assert count_lines_in("nonexistent_file.txt") is None


def test__count_lines_in__return_zero_when_empty_file(make_file):
    filepath = "empty_file.txt"
    make_file(filepath, lines=0, comments=0)

    assert count_lines_in(filepath) == 0


@pytest.mark.parametrize("comments", [1, 10, 100])
def test__count_lines_in__return_zero_when_file_with_only_comments(make_file, comments):
    filepath = "comments_file.txt"
    make_file(filepath, lines=0, comments=comments)

    assert count_lines_in(filepath) == 0


@pytest.mark.parametrize(
    "lines, comments",
    [(1, 1), (10, 2), (150, 33)],
)
def test__count_lines_in__return_correct_value_when_file_with_lines_and_comments(
    make_file, lines, comments
):
    filepath = "mixed_file.txt"
    make_file(filepath, lines=lines, comments=comments)

    assert count_lines_in(filepath) == lines


@pytest.mark.parametrize("lines", [1, 10, 100])
def test__count_lines_in__return_correct_value_when_file_with_only_lines(make_file, lines):
    filepath = "lines_file.txt"
    make_file(filepath, lines=lines, comments=0)

    assert count_lines_in(filepath) == lines
