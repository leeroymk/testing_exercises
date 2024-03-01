import datetime

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense


@pytest.fixture
def cards():
    return [BankCard("1234", "Vasya"), BankCard("0123", "Petya")]


@pytest.mark.parametrize(
    "sms, expected_amount",
    [
        (
            SmsMessage(
                "100 200.5, 1234 01.01.20 12:00 12:01 shop",
                "Ivan",
                datetime.datetime(2022, 1, 1, 12, 0),
            ),
            100,
        )
    ],
)
def test__parse_ineco_expense__return_correct_amount(sms, cards, expected_amount):
    expense = parse_ineco_expense(sms, cards)
    assert expense.amount == expected_amount


@pytest.mark.parametrize(
    "sms, expected_spent_at",
    [
        (
            SmsMessage(
                "100 200.5, 1234 01.01.20 12:00 shop",
                "Ivan",
                datetime.datetime(2022, 1, 1, 12, 0),
            ),
            datetime.datetime(2020, 1, 1, 12, 0),
        ),
        (
            SmsMessage(
                "100 200.5, 1234 02.01.20 13:00 Cafe",
                "Ivan",
                datetime.datetime(2022, 1, 1, 12, 0),
            ),
            datetime.datetime(2020, 1, 2, 13, 0),
        ),
    ],
)
def test__parse_ineco_expense__return_correct_spent_at(sms, cards, expected_spent_at):
    expense = parse_ineco_expense(sms, cards)
    assert expense.spent_at == expected_spent_at
