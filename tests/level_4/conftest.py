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
        telegram_account = "@" + faker.pystr() if telegram_account is NOT_SET else telegram_account
        return Student(
            first_name=first_name,
            last_name=last_name,
            telegram_account=telegram_account,
        )

    return inner


@pytest.fixture
def make_file():
    filepath_var = None

    def inner(filepath, lines, comments):
        nonlocal filepath_var
        filepath_var = filepath
        with open(filepath, "w") as file:
            for _ in range(lines):
                file.write(f"line {_}\n")
            for _ in range(comments):
                file.write(f"# comment {_}\n")

    yield inner

    os.remove(filepath_var)


@pytest.fixture
def create_config():
    def inner(filepath, content):
        with open(filepath, "w") as file:
            file.write("[tool:app-config]\n")
            file.write(content)

    yield inner
