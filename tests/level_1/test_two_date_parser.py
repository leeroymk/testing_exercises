import datetime

import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.fixture
def today():
    return datetime.date.today()


@pytest.fixture
def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)


@pytest.mark.parametrize("date_str, time_str", [("today", "12:00"), ("today", "00:00")])
def test__compose_datetime_from__today(date_str, time_str, today):
    expected_datetime = datetime.datetime(
        today.year,
        today.month,
        today.day,
        int(time_str.split(":")[0]),
        int(time_str.split(":")[1]),
    )
    assert compose_datetime_from(date_str, time_str) == expected_datetime


@pytest.mark.parametrize(
    "date_str, time_str", [("tomorrow", "12:00"), ("tomorrow", "00:00")]
)
def test__compose_datetime_from__tomorrow(date_str, time_str, tomorrow):
    expected_datetime = datetime.datetime(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
        int(time_str.split(":")[0]),
        int(time_str.split(":")[1]),
    )
    assert compose_datetime_from(date_str, time_str) == expected_datetime
