import datetime

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__empty_history_returns_empty_list():
    assert find_fraud_expenses([]) == []


def test__find_fraud_expenses__over_3_payments_less_or_equal_5000_in_one_time_returns_fraud_list(
    expense_object,
):
    expense = expense_object(
        amount=5000,
    )

    assert find_fraud_expenses([expense, expense, expense]) == [
        expense,
        expense,
        expense,
    ]


def test__find_fraud_expenses__two_purchases_below_max_amount_returns_empty_list(
    expense_object,
):
    expense = expense_object(
        amount=500,
    )

    assert find_fraud_expenses([expense, expense]) == []


def test__find_fraud_expenses__three_purchases_below_max_amount_in_different_days_returns_empty_list(
    expense_object,
):
    expense_1 = expense_object(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 1),
    )
    expense_2 = expense_object(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 2),
    )
    expense_3 = expense_object(
        amount=500,
        spent_at=datetime.datetime(2024, 3, 3),
    )

    assert find_fraud_expenses([expense_1, expense_2, expense_3]) == []
