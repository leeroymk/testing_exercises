import datetime

import pytest

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__no_fraud_empty_history():
    assert find_fraud_expenses([]) == []


@pytest.mark.parametrize("amount", [3000, 5000])
def test__find_fraud_expenses__fraud_found_over_3_payments_less_or_equal_5000_at_one_time(
    make_expense, amount
):
    expenses = [
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=amount,
        ),
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=amount,
        ),
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=amount,
        ),
    ]

    assert find_fraud_expenses(expenses) == expenses


def test__find_fraud_expenses__no_fraud_found_over_3_payments_over_5000_at_one_time(
    make_expense,
):
    expenses = [
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=6000,
        ),
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=6000,
        ),
        make_expense(
            spent_in="chinar",
            spent_at=datetime.datetime(2024, 3, 1),
            amount=6000,
        ),
    ]

    assert find_fraud_expenses(expenses) == []


def test__find_fraud_expenses__no_fraud_found_2_equal_purchases_below_max_amount_at_one_day(
    make_expense,
):
    expenses = [
        make_expense(
            amount=500,
            spent_at=datetime.datetime(2024, 3, 1),
        ),
        make_expense(
            amount=500,
            spent_at=datetime.datetime(2024, 3, 1),
        ),
    ]

    assert find_fraud_expenses(expenses) == []


def test__find_fraud_expenses__no_fraud_found_3_purchases_below_max_amount_at_different_days(
    make_expense,
):
    expenses = [
        make_expense(
            amount=500,
            spent_at=datetime.datetime(2024, 3, 1),
        ),
        make_expense(
            amount=500,
            spent_at=datetime.datetime(2024, 3, 2),
        ),
        make_expense(
            amount=500,
            spent_at=datetime.datetime(2024, 3, 3),
        ),
    ]

    assert find_fraud_expenses(expenses) == []
