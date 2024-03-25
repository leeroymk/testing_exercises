from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


def test__guess_expense_category__return_supermarket_if_category_is_supermarket(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.SUPERMARKET,
        spent_in="chinar",
    )
    assert guess_expense_category(expense) == ExpenseCategory.SUPERMARKET


def test__guess_expense_category__return_theatres_if_category_is_theatres_movies_culture(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
        spent_in="tomsarkgh",
    )
    assert guess_expense_category(expense) == ExpenseCategory.THEATRES_MOVIES_CULTURE


def test__guess_expense_category__return_online_subscriptions_if_category_is_online_subscriptions(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
        spent_in="netflix",
    )
    assert guess_expense_category(expense) == ExpenseCategory.ONLINE_SUBSCRIPTIONS


def test__guess_expense_category__return_medicine_pharmacy_if_category_is_medicine_pharmacy(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.MEDICINE_PHARMACY,
        spent_in="alfa-pharm",
    )
    assert guess_expense_category(expense) == ExpenseCategory.MEDICINE_PHARMACY


def test__guess_expense_category__return_transport_if_category_is_transport(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.TRANSPORT,
        spent_in="yandex go",
    )
    assert guess_expense_category(expense) == ExpenseCategory.TRANSPORT


def test__guess_expense_category__return_bar_restaurant_if_category_is_bar_restaurant(
    expense_object,
):
    expense = expense_object(
        category=ExpenseCategory.BAR_RESTAURANT,
        spent_in="doc",
    )
    assert guess_expense_category(expense) == ExpenseCategory.BAR_RESTAURANT


def test__guess_expense_category__return_none_if_category_is_none(
    expense_object,
):
    expense = expense_object(
        category=None,
        spent_in="wildberries",
    )
    assert guess_expense_category(expense) is None
