import pytest


@pytest.fixture
def good_words():
    return {"good", "nice", "beautiful"}


@pytest.fixture
def bad_words():
    return {"bad", "awful", "terrible"}
