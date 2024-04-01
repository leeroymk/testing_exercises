import datetime

import pytest

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__return_true_for_three_months_purchases(make_expense, make_spent_in):
    first_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 3, 1),
    )
    second_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 4, 1),
    )
    third_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 5, 1),
    )

    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is True


def test__is_subscription__return_false_when_lt_three_months_purchases(
    make_expense, make_spent_in
):
    first_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 3, 1),
    )
    second_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 3, 2),
    )
    third_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2024, 4, 1),
    )

    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is False


@pytest.mark.xfail(reason="is the right behavior")
def test__is_subscription__return_false_when_has_month_without_payment(
    make_expense, make_spent_in
):
    first_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2023, 1, 1),
    )
    second_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2023, 3, 1),
    )
    third_expense = make_expense(
        spent_in=make_spent_in,
        spent_at=datetime.datetime(2023, 12, 1),
    )
    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is False


def test__is_subscription__return_false_when_payment_in_different_places(make_expense):
    first_expense = make_expense(spent_in="marketplace")
    second_expense = make_expense(spent_in="zoo")
    third_expense = make_expense(spent_in="school")
    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is False
