import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (90.2, 8.3, 1.4, (None, None)),
        (55.5, 0.0, 2.2, (None, None)),
    ],
)
def test__solve_square_equation__discriminant_lt_zero_return_None_None(
    square_coefficient, linear_coefficient, const_coefficient, expected
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (0.0, 2.0, 2.2, (-1.1, None)),
        (0.0, 2.0, 1.0, (-0.5, None)),
    ],
)
def test__solve_square_equation__square_coef_zero_linear_coef_not_zero_return_number_and_None(
    square_coefficient, linear_coefficient, const_coefficient, expected
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (0.0, 0.0, 1.0, (None, None)),
        (0.0, 0.0, 3.0, (None, None)),
    ],
)
def test__solve_square_equation__square_coef_zero_linear_coef_zero_return_None_and_None(
    square_coefficient, linear_coefficient, const_coefficient, expected
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected",
    [
        (2.0, 4.0, 1.0, (-1.7071067811865475, -0.2928932188134524)),
        (2.0, 4.0, 0.0, (-2.0, 0.0)),
    ],
)
def test__solve_square_equation__square_coef_not_zero_linear_coef_not_zero_return_two_numbers(
    square_coefficient, linear_coefficient, const_coefficient, expected
):
    assert (
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
        == expected
    )
