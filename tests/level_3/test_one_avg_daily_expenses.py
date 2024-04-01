import datetime
import decimal
from statistics import (
    StatisticsError,
)

import pytest

from functions.level_3.one_avg_daily_expenses import (
    calculate_average_daily_expenses,
)


def test__calculate_average_daily_expenses__correct_average_when_spent_in_different_days(
    make_expense,
):
    expenses = [
        make_expense(amount=100, spent_at=datetime.datetime(2024, 3, 1)),
        make_expense(amount=100, spent_at=datetime.datetime(2024, 4, 1)),
        make_expense(amount=100, spent_at=datetime.datetime(2024, 5, 1)),
    ]

    assert calculate_average_daily_expenses(expenses) == decimal.Decimal(100)


def test__calculate_average_daily_expenses__correct_average_when_spent_in_one_day(
    make_expense,
):
    expenses = [
        make_expense(amount=100, spent_at=datetime.datetime(2024, 5, 1)),
        make_expense(amount=200, spent_at=datetime.datetime(2024, 5, 1)),
        make_expense(amount=300, spent_at=datetime.datetime(2024, 5, 1)),
    ]

    assert calculate_average_daily_expenses(expenses) == decimal.Decimal(600)


def test__calculate_average_daily_expenses__error_raised_when_no_daily_expences():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])
