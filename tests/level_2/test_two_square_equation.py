import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "a, b, c",
    [
        (90.2, 8.3, 1.4),
        (55.5, 0.0, 2.2),
    ],
)
def test__solve_square_equation__return_no_roots_if_discriminant_lt_zero(a, b, c):
    assert solve_square_equation(a, b, c) == (None, None)


@pytest.mark.parametrize(
    "b, c, root",
    [
        (2.0, 2.2, (-1.1, None)),
        (2.5, 1.0, (-0.4, None)),
    ],
)
def test__solve_square_equation__return_one_root_with_zeroes_in_square_and_linear_coefficients(
    b, c, root
):
    assert solve_square_equation(0.0, b, c) == root


@pytest.mark.parametrize(
    "c",
    [1.0, -57.2, 0.0],
)
def test__solve_square_equation__return_no_roots__square_coef_zero_linear_coef_zero(c):
    assert solve_square_equation(0.0, 0.0, c) == (None, None)


@pytest.mark.parametrize(
    "a, b, c, roots",
    [
        (1.5, 6.5, 3.0, (-3.808142966966017, -0.525190366367316)),
        (2.0, 4.0, 0.0, (-2.0, 0.0)),
    ],
)
def test__solve_square_equation__return_two_numbers_if_square_coef_not_zero_linear_coef_not_zero(
    a, b, c, roots
):
    assert solve_square_equation(a, b, c) == roots
