import pytest
from evaluator import evaluate_expression


def test_simple_addition():
    assert evaluate_expression("2 + 3") == 5.0


def test_simple_subtraction():
    assert evaluate_expression("5 - 3") == 2.0


def test_simple_multiplication():
    assert evaluate_expression("2 * 3") == 6.0


def test_simple_division():
    assert evaluate_expression("6 / 2") == 3.0


def test_complex_expression():
    assert evaluate_expression("(2 + 3) * 4 - 6 / 2") == 17.0


def test_negative_number():
    assert evaluate_expression("-3 + 5") == 2.0


def test_expression_with_spaces():
    assert evaluate_expression("   2  *   (  3  +  4 ) ") == 14.0


def test_invalid_expression():
    with pytest.raises(ValueError):
        evaluate_expression("2 +")


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_expression("6 / 0")


if __name__ == "__main__":
    pytest.main()
