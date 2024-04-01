import datetime
import decimal
import typing as t

import pytest

from functions.level_3.models import BankCard, Expense, ExpenseCategory

NOT_SET: t.Any = "____"


def defval(value: t.Any, default: t.Any) -> t.Any:
    return default if value is NOT_SET else value


@pytest.fixture
def make_card(faker):
    return BankCard(last_digits=faker.credit_card_number()[:-4], owner=faker.name())


@pytest.fixture
def make_spent_at(faker):
    return faker.past_date()


@pytest.fixture
def make_spent_in(faker):
    return faker.company()


@pytest.fixture
def make_amount_lt_five_thousand(faker):
    return faker.pyfloat(max_value=5000)


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
        amount = defval(amount, faker.pyfloat(left_digits=3, right_digits=2, positive=True))
        currency = defval(currency, faker.currency_code())
        card = defval(card, make_card)
        spent_in = defval(spent_in, make_spent_in)
        spent_at = defval(spent_at, faker.past_date())
        category = defval(category, faker.enum(ExpenseCategory))

        return Expense(
            amount=decimal.Decimal(str(amount)),
            currency=currency,
            card=card,
            spent_in=spent_in,
            spent_at=spent_at,
            category=category,
        )

    return inner
