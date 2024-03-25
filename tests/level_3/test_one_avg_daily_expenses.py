import datetime
import decimal

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__return_correct_average(expense_object):
    expense_1 = expense_object(spent_at=datetime.datetime(2024, 3, 1))
    expense_2 = expense_object(spent_at=datetime.datetime(2024, 4, 1))
    expense_3 = expense_object(spent_at=datetime.datetime(2024, 5, 1))

    assert calculate_average_daily_expenses(
        [expense_1, expense_2, expense_3]
    ) == decimal.Decimal(100)
