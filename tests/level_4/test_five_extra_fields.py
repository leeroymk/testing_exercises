import pytest

from functions.level_4.five_extra_fields import fetch_extra_fields_configuration
from tests.level_4.conftest import remove_temp_file


def test__fetch_extra_fields_configuration__return_empty_dict_when_no_config():
    assert fetch_extra_fields_configuration("nonexistent_config.ini") == {}


def test__fetch_extra_fields_configuration__return_empty_dict_when_config_has_no_extra_fields(
    create_config,
):
    filepath = "empty_config.ini"
    create_config(filepath, "")

    assert fetch_extra_fields_configuration(filepath) == {}

    remove_temp_file(filepath)


@pytest.mark.parametrize(
    "field, value",
    [("field_one", "value_one"), ("field_two", "value_two"), ("field_three", "value_three")],
)
def test__fetch_extra_fields_configuration__return_empty_dict_when_config_has_invalid_fields(
    create_config, field, value
):
    filepath = "empty_config.ini"
    create_config(filepath, f"invalid_fields = {field}: {value}")

    assert fetch_extra_fields_configuration(filepath) == {}

    remove_temp_file(filepath)


@pytest.mark.parametrize("type_value", ["int", "str", "dict", "list", "set", "tuple"])
def test__fetch_extra_fields_configuration__return_valid_dict_when_config_has_one_extra_field(
    create_config, type_value
):
    filepath = "config_one_extra_field.ini"
    content = f"extra_fields = first_field: {type_value}"
    create_config(filepath, content)

    assert fetch_extra_fields_configuration(filepath) == {"first_field": eval(type_value)}

    remove_temp_file(filepath)


def test__fetch_extra_fields_configuration__return_valid_dict_when_config_has_few_extra_fields(
    create_config,
):
    filepath = "config_few_extra_fields.txt"
    content = "extra_fields = first_field: int\n    second_field: str\n    third_field: list\n"
    create_config(filepath, content)

    assert fetch_extra_fields_configuration(filepath) == {
        "first_field": int,
        "second_field": str,
        "third_field": list,
    }

    remove_temp_file(filepath)


def test__fetch_extra_fields_configuration__raise_error_when_invalid_type(create_config):
    filepath = "incorrect_type_config.ini"
    content = "extra_fields = first_field: error\n"
    create_config(filepath, content)

    with pytest.raises(NameError):
        assert fetch_extra_fields_configuration(filepath)

    remove_temp_file(filepath)
