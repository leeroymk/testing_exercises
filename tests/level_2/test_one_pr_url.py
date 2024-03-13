import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url",
    [
        "https://github.com/leeroymk/testing_exercises/pull/1",
        "https://github.com/user/repo/pull/2",
    ],
)
def test__is_github_pull_request_url__valid_pull_request_return_true(url):
    assert is_github_pull_request_url(url) is True


@pytest.mark.parametrize(
    "url",
    [
        "https://gitlab.com/",
        "https://onlyfans.com/",
        "https://localhost/",
    ],
)
def test__is_github_pull_request_url__invalid_site_return_false(
    url,
):
    assert is_github_pull_request_url(url) is False


@pytest.mark.parametrize(
    "url",
    [
        "https://github.com/leeroymk/testing_exercises/pull/1/merge",
        "https://github.com/wei/pull/pull/572/commits",
    ],
)
def test__is_github_pull_request_url__invalid_pull_request_return_false(url):
    assert is_github_pull_request_url(url) is False
