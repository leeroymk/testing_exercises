import typing as t

from faker import Faker
import pytest

from functions.level_4.two_students import Student


NOT_SET: t.Any = "____"

faker = Faker()


@pytest.fixture
def make_student(faker):
    def inner(
        first_name: str = NOT_SET,
        last_name: str = NOT_SET,
        telegram_account: str | None = NOT_SET,
    ):
        first_name = faker.first_name() if first_name == NOT_SET else first_name
        last_name = faker.last_name() if last_name == NOT_SET else last_name
        telegram_account = (
            "@" + faker.simple_profile()["username"]
            if telegram_account == NOT_SET
            else telegram_account
        )
        return Student(
            first_name=first_name,
            last_name=last_name,
            telegram_account=telegram_account,
        )

    return inner
