import pytest
from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize("name", ["text", "not_text", "kinda_text"])
def test__delete_remove_brackets_quotes__cut_correctly_if_in_brackets_and_spaces(
    name,
):
    assert delete_remove_brackets_quotes("{ " + name + " }") == name


@pytest.mark.xpass(reason="is the right behavior?")
def test__delete_remove_brackets_quotes__cut_incorrectly_if_in_brackets_no_spaces():
    assert delete_remove_brackets_quotes("{" + "text" + "}") == "ex"


@pytest.mark.parametrize("name", ["t", "te", "tex"])
def test__delete_remove_brackets_quotes__return_name_if_no_brackets(name):
    assert delete_remove_brackets_quotes(name) == name


def test__delete_remove_brackets_quotes__raises_exception_if_name_is_empty():
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes("")


@pytest.mark.parametrize("name", ["{}", "{ }", "{  }"])
def test_delete_remove_brackets_quotes__return_empty_string_if_name_is_empty(name):
    assert delete_remove_brackets_quotes(name) == ""
