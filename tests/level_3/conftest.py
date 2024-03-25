import datetime
import decimal

import pytest

from functions.level_3.models import BankCard, Expense, ExpenseCategory


@pytest.fixture
def expense_object():
    def expense_factory(
        amount=100,
        currency="RUB",
        card=BankCard(last_digits="1234", owner="Petya"),
        spent_in="chinar",
        spent_at=datetime.datetime(2024, 3, 1),
        category=ExpenseCategory.SUPERMARKET,
    ):
        return Expense(
            amount=decimal.Decimal(amount),
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category,
        )

    return expense_factory
