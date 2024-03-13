import pytest

from functions.level_1.three_url_builder import build_url


def test__build_url__get_params_is_none():
    assert build_url("host_name", "relative/url", None) == "host_name/relative/url"


def test__build_url__get_params_is_not_none():
    assert (
        build_url("host_name", "relative_url", {"key1": "value1"})
        == "host_name/relative_url?key1=value1"
    )


@pytest.mark.parametrize("host_name", ["host_name", "www.somesite.com", "localhost"])
def test__build_url__host_name_return_as_is(host_name):
    assert (
        build_url(host_name, "relative/url", {"key1": "value1"})
        == f"{host_name}/relative/url?key1=value1"
    )


@pytest.mark.parametrize("relative_url", ["relative-url", "relative-url-2"])
def test__build_url__relative_url_return_as_is(relative_url):
    assert (
        build_url("host_name", relative_url, {"key1": "value1"})
        == f"host_name/{relative_url}?key1=value1"
    )
