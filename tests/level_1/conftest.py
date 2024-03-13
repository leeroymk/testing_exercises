import datetime

import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage


@pytest.fixture
def today():
    return datetime.date.today()


@pytest.fixture
def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)


@pytest.fixture
def cards():
    return [BankCard("1234", "Vasya"), BankCard("0123", "Petya")]


@pytest.fixture
def make_sms():
    def make_sms_function(text=None, author=None, sent_at=None):
        return SmsMessage(text, author, sent_at)

    return make_sms_function
