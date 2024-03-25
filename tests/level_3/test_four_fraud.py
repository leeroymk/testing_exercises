import datetime

import pytest

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__empty_history_return_empty_list():
    assert find_fraud_expenses([]) == []


@pytest.mark.parametrize("amount", [3000, 5000])
def test__find_fraud_expenses__over_3_payments_less_or_equal_5000_in_one_time_are_fraud(
    make_expense, amount
):
    expense_1 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=amount,
    )
    expense_2 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=amount,
    )
    expense_3 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=amount,
    )

    assert find_fraud_expenses([expense_1, expense_2, expense_3]) == [
        expense_1,
        expense_2,
        expense_3,
    ]


def test__find_fraud_expenses__over_3_payments_over_5000_in_one_time_are_not_fraud(
    make_expense,
):
    expense_1 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=6000,
    )
    expense_2 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=6000,
    )
    expense_3 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        amount=6000,
    )

    assert find_fraud_expenses([expense_1, expense_2, expense_3]) == []


def test__find_fraud_expenses__2_equal_purchases_below_max_amount_in_one_day_are_not_fraud(
    make_expense,
):
    expense_1 = make_expense(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 1),
    )
    expense_2 = make_expense(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 1),
    )

    assert find_fraud_expenses([expense_1, expense_2]) == []


def test__find_fraud_expenses__3_purchases_below_max_amount_in_different_days_are_not_fraud(
    make_expense,
):
    expense_1 = make_expense(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 1),
    )
    expense_2 = make_expense(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 2),
    )
    expense_3 = make_expense(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 3),
    )

    assert find_fraud_expenses([expense_1, expense_2, expense_3]) == []
