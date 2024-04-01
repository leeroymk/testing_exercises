import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


def test__guess_expense_category__return_none_if_no_spent_in(make_expense):
    expense = make_expense(category=None, spent_in="wildberries")
    assert guess_expense_category(expense) is None


@pytest.mark.parametrize(
    "spent_in, expected",
    [
        ("asador", ExpenseCategory.BAR_RESTAURANT),
        ("chinar", ExpenseCategory.SUPERMARKET),
        ("apple.com/bill", ExpenseCategory.ONLINE_SUBSCRIPTIONS),
        ("farm", ExpenseCategory.MEDICINE_PHARMACY),
        ("tomsarkgh", ExpenseCategory.THEATRES_MOVIES_CULTURE),
        ("gg platform", ExpenseCategory.TRANSPORT),
    ],
)
def test__guess_expense_category__return_correct_name(spent_in, expected, make_expense):
    assert guess_expense_category(make_expense(spent_in=spent_in)) == expected
