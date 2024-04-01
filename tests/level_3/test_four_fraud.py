import datetime

import pytest

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__return_empty_list_for_empty_history():
    assert find_fraud_expenses([]) == []


# parametrize or fixture is better?
@pytest.mark.parametrize("amount", [3000, 5000])
def test__find_fraud_expenses__find_fraud_gt_three_payments_lt_or_eq_five_thousand_in_one_time_and_place(
    make_expense, amount, make_spent_at, make_spent_in
):
    expenses = [
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
    ]

    assert find_fraud_expenses(expenses) == expenses


@pytest.mark.parametrize("amount", [6000, 100000])
def test__find_fraud_expenses__find_no_fraud_gt_three_payments_over_five_thousand_in_one_time_and_place(
    make_expense, make_spent_at, make_spent_in, amount
):
    expenses = [
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
        make_expense(spent_in=make_spent_in, spent_at=make_spent_at, amount=amount),
    ]

    assert find_fraud_expenses(expenses) == []


@pytest.mark.parametrize("amount", [4999, 1, 500])
def test__find_fraud_expenses__find_no_fraud_for_lt_three_expenses(
    make_expense, amount, make_spent_at
):
    expenses = [
        make_expense(amount=amount, spent_at=make_spent_at),
        make_expense(amount=amount, spent_at=make_spent_at),
    ]

    assert find_fraud_expenses(expenses) == []


# parametrize or fixture is better?
def test__find_fraud_expenses__find_no_fraud_for_different_days_expenses(
    make_expense, make_amount_lt_five_thousand
):
    expenses = [
        make_expense(
            amount=make_amount_lt_five_thousand,
            spent_at=datetime.datetime(2024, 3, 1),
        ),
        make_expense(
            amount=make_amount_lt_five_thousand,
            spent_at=datetime.datetime(2024, 3, 2),
        ),
        make_expense(
            amount=make_amount_lt_five_thousand,
            spent_at=datetime.datetime(2024, 3, 3),
        ),
    ]

    assert find_fraud_expenses(expenses) == []
