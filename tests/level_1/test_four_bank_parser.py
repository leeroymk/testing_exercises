import datetime
import decimal

import pytest

from functions.level_1.four_bank_parser import (BankCard, Expense, SmsMessage,
                                                parse_ineco_expense)


@pytest.mark.parametrize(
    "sms, cards, expected_result",
    [
        (
            SmsMessage(
                "100 000.500, 1234 01.01.20 12:00 12:01",
                "Иван",
                datetime.datetime(2022, 1, 1, 12, 0),
            ),
            [BankCard("1234", "Иван Иванов")],
            Expense(
                amount=decimal.Decimal("100"),
                card=BankCard(last_digits="1234", owner="Иван Иванов"),
                spent_in="12:01",
                spent_at=datetime.datetime(2020, 1, 1, 12, 0),
            ),
        ),
        (
            SmsMessage(
                "200 000.500, 5678 02.02.20 13:00 13:01",
                "Петр",
                datetime.datetime(2022, 1, 2, 14, 30),
            ),
            [BankCard("5678", "Петр Петров")],
            Expense(
                amount=decimal.Decimal("200"),
                card=BankCard(last_digits="5678", owner="Петр Петров"),
                spent_in="13:01",
                spent_at=datetime.datetime(2020, 2, 2, 13, 0),
            ),
        ),
        (
            SmsMessage(
                "300 000.500, 9012 03.03.20 14:00 14:01",
                "Анна",
                datetime.datetime(2022, 1, 3, 16, 45),
            ),
            [BankCard("9012", "Анна Смирнова")],
            Expense(
                amount=decimal.Decimal("300"),
                card=BankCard(last_digits="9012", owner="Анна Смирнова"),
                spent_in="14:01",
                spent_at=datetime.datetime(2020, 3, 3, 14, 0),
            ),
        ),
    ],
)
def test_parse_ineco_expense(sms, cards, expected_result):
    assert parse_ineco_expense(sms, cards) == expected_result
