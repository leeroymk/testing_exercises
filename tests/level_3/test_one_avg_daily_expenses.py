import datetime
import decimal
from statistics import StatisticsError

import pytest

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__return_correct_average_in_different_days(
    make_expense,
):
    expense_1 = make_expense(amount=100, spent_at=datetime.datetime(2024, 3, 1))
    expense_2 = make_expense(amount=100, spent_at=datetime.datetime(2024, 4, 1))
    expense_3 = make_expense(amount=100, spent_at=datetime.datetime(2024, 5, 1))

    assert calculate_average_daily_expenses(
        [expense_1, expense_2, expense_3]
    ) == decimal.Decimal(100)


def test__calculate_average_daily_expenses__return_correct_average_in_one_day(
    make_expense,
):
    expense_1 = make_expense(amount=100, spent_at=datetime.datetime(2024, 5, 1))
    expense_2 = make_expense(amount=200, spent_at=datetime.datetime(2024, 5, 1))
    expense_3 = make_expense(amount=300, spent_at=datetime.datetime(2024, 5, 1))

    assert calculate_average_daily_expenses(
        [expense_1, expense_2, expense_3]
    ) == decimal.Decimal(600)


def test__calculate_average_daily_expenses__empty_list_raises_statistics_error():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])
