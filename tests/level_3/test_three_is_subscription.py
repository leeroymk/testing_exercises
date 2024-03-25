import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__is_subscription_3_plus_purchases_in_1_place_at_most_once_a_month(
    make_expense,
):
    first_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
    )
    second_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 4, 1),
    )
    third_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 5, 1),
    )

    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is True


def test__is_subscription__is_not_subscription_3_plus_purchases_in_1_place_at_most_once_a_month(
    make_expense,
):
    first_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
    )
    second_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 2),
    )
    third_expense = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 4, 1),
    )

    assert is_subscription(first_expense, [first_expense, second_expense, third_expense]) is False


def test__is_subscription__is_not_subscription_less_than_3_purchases_in_1_place(
    make_expense,
):
    first_expense = make_expense(spent_in="chinar")
    second_expense = make_expense(spent_in="chinar")
    assert is_subscription(first_expense, [first_expense, second_expense]) is False
