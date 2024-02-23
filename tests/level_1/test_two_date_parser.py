from datetime import date, datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize(
    "date_str, time_str, expected_result",
    [
        (
            "tomorrow",
            "10:15",
            datetime(
                date.today().year, date.today().month, date.today().day + 1, 10, 15
            ),
        ),
        (
            "othertime",
            "10:15",
            datetime(date.today().year, date.today().month, date.today().day, 10, 15),
        ),
    ],
)
def test_compose_datetime_from(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


@pytest.mark.parametrize(
    "date_str, time_str, expected_exception",
    [
        ("tomorrow", "10-15", ValueError),
        ("tomorrow", None, AttributeError),
    ],
)
def test_compose_datetime_from_error(date_str, time_str, expected_exception):
    with pytest.raises(expected_exception):
        compose_datetime_from(date_str, time_str)
