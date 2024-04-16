import os
import typing as t

import pytest

from functions.level_4.two_students import Student

NOT_SET: t.Any = "____"


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


@pytest.fixture
def create_file():
    def inner(filepath, lines, comments):
        with open(filepath, "w") as file:
            for _ in range(lines):
                file.write(f"line {_}\n")
            for _ in range(comments):
                file.write(f"# comment {_}\n")

    return inner


@pytest.fixture
def create_config():
    def inner(filepath, content):
        with open(filepath, "w") as file:
            file.write("[tool:app-config]\n")
            file.write(content)

    return inner


def remove_temp_file(filepath):
    os.remove(filepath)
