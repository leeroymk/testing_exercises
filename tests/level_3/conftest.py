import datetime
import decimal
import typing as t

import pytest
from faker import Faker

from functions.level_3.models import BankCard, Expense, ExpenseCategory

NOT_SET: t.Any = "____"

faker = Faker()


@pytest.fixture
def make_expense(faker):
    def inner(
        amount: float = NOT_SET,
        currency: str = NOT_SET,
        card: BankCard = NOT_SET,
        spent_in: str = NOT_SET,
        spent_at: datetime.datetime = NOT_SET,
        category: ExpenseCategory = NOT_SET,
    ):
        amount = (
            faker.pyfloat(left_digits=3, right_digits=2, positive=True)
            if amount is NOT_SET
            else amount
        )
        currency = faker.currency_code() if currency is NOT_SET else currency
        card = (
            BankCard(last_digits=faker.credit_card_number()[-4:], owner=faker.name())
            if card is NOT_SET
            else card
        )
        spent_in = faker.company() if spent_in is NOT_SET else spent_in
        spent_at = faker.date_time_this_year() if spent_at is NOT_SET else spent_at
        category = (
            faker.random_element(elements=ExpenseCategory)
            if category is NOT_SET
            else category
        )

        return Expense(
            amount=decimal.Decimal(str(amount)),
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category,
        )

    return inner
