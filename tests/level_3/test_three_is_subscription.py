import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__three_plus_purchases_in_one_location_and_not_more_than_once_in_month_is_subscription(
    make_expense,
):
    expense_1 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
    )
    expense_2 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 4, 1),
    )
    expense_3 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 5, 1),
    )

    assert is_subscription(expense_1, [expense_1, expense_2, expense_3]) is True


def test__is_subscription__three_plus_purchases_in_one_location_and_more_than_once_in_month_is_not_subscription(
    make_expense,
):
    expense_1 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
    )
    expense_2 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 2),
    )
    expense_3 = make_expense(
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 4, 1),
    )

    assert is_subscription(expense_1, [expense_1, expense_2, expense_3]) is False


def test__is_subscription__less_than_three_purchases_in_one_location_is_not_subscription(
    make_expense,
):
    expense_1 = make_expense(spent_in="chinar")
    expense_2 = make_expense(spent_in="chinar")
    assert is_subscription(expense_1, [expense_1, expense_2]) is False
