import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name, relative_url, get_params, expected_url",
    [
        ("www.somesite.com", "relative/url", None, "www.somesite.com/relative/url"),
        (
            "www.somesite.com",
            "relative/url",
            {"key1": "value1"},
            "www.somesite.com/relative/url?key1=value1",
        ),
        (
            "www.somesite.com",
            "relative/url",
            {"key1": "value1", "key2": "value2"},
            "www.somesite.com/relative/url?key1=value1&key2=value2",
        ),
        (
            "www.somesite.com",
            "relative/url",
            {"key1": "value1", "key2": "value2", "key3": "value3"},
            "www.somesite.com/relative/url?key1=value1&key2=value2&key3=value3",
        ),
    ],
)
def test_build_url(host_name, relative_url, get_params, expected_url):
    url = build_url(host_name, relative_url, get_params)
    assert url == expected_url
