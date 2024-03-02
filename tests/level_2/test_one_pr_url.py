import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://github.com/leeroymk/testing_exercises/pull/1", True),
        ("https://github.com/user/repo/pull/2", True),
    ],
)
def test__is_github_pull_request_url__valid_pull_request_return_true(url, expected):
    assert is_github_pull_request_url(url) == expected


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://gitlab.com/", False),
        ("https://onlyfans.com/", False),
        ("https://localhost/", False),
    ],
)
def test__is_github_pull_request_url__invalid_site_return_false(url, expected):
    assert is_github_pull_request_url(url) == expected


@pytest.mark.parametrize(
    "url, expected",
    [
        ("https://github.com/leeroymk/testing_exercises/pull/1/merge", False),
        ("https://github.com/wei/pull/pull/572/commits", False),
    ],
)
def test__is_github_pull_request_url__invalid_pull_request_return_false(url, expected):
    assert is_github_pull_request_url(url) == expected
