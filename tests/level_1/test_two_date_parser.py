import pytest

from functions.level_1.two_date_parser import compose_datetime_from


@pytest.mark.parametrize("time_str", ["12:00", "00:00", "23:59"])
def test__compose_datetime_from__today_different_time_returns_today(time_str, today):
    assert compose_datetime_from("today", time_str).date() == today


@pytest.mark.parametrize("date_str", ["someday", "not-tomorrow"])
def test__compose_datetime_from__not_tomorrow_day_returns_today(date_str, today):
    assert compose_datetime_from(date_str, "12:00").date() == today


@pytest.mark.parametrize("time_str", ["12:00", "00:00", "23:59"])
def test__compose_datetime_from__any_time_tomorrow_returns_tomorrow(time_str, tomorrow):
    assert compose_datetime_from("tomorrow", time_str).date() == tomorrow


@pytest.mark.parametrize("time_str, expected", [("12:00", 12), ("00:00", 0), ("23:59", 23)])
def test__compose_datetime_from__hour_parsing_valid(time_str, expected):
    assert compose_datetime_from("tomorrow", time_str).hour == expected


@pytest.mark.parametrize(
    "time_str, expected",
    [
        ("12:00", 0),
        ("00:31", 31),
        ("23:59", 59),
    ],
)
def test__compose_datetime_from__minutes_parsing_valid(time_str, expected):
    assert compose_datetime_from("today", time_str).minute == expected
