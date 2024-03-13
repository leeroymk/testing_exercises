import decimal

import pytest

from functions.level_1.four_bank_parser import parse_ineco_expense


@pytest.mark.parametrize(
    "sms, amount",
    [
        ("100 200.5, 1234 01.01.20 12:00 12:01 shop", 100),
        ("-20 200.5, 0123 01.01.20 12:00 12:01 shop", -20),
    ],
)
def test__parse_ineco_expense__return_correct_amount(sms, amount, make_sms, cards):
    sms_message = make_sms(text=sms)
    expense = parse_ineco_expense(sms_message, cards)
    assert expense.amount == decimal.Decimal(amount)


@pytest.mark.parametrize(
    "sms, expected_spent_at",
    [
        ("100 200.5, 1234 01.01.20 12:00 12:01 shop", "2020-01-01T12:00:00"),
        ("200 200.5, 0123 13.03.24 16:36 12:01 shop", "2024-03-13T16:36:00"),
    ],
)
def test__parse_ineco_expense__return_correct_spent_at(
    sms, expected_spent_at, make_sms, cards
):
    sms_message = make_sms(text=sms)
    expense = parse_ineco_expense(sms_message, cards)
    assert expense.spent_at.isoformat() == expected_spent_at
