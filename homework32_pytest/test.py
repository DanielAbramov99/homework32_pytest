import time
from webbrowser import Error

# testabile

import pytest
from pyexpat import ExpatError

import calculator

from calc import power, sqrt, factorial


# d and e
def test_power_function():
    result = power(2, 4)
    assert result == 16, f"Expected 16, but got {result}"
    print("test_power_function passed.")
    result2 = power(3, 2)
    assert result2 == 9, f"Expected 9, but got {result2}"


test_power_function()


# f
def test_sqrt_function():
    result = sqrt(25)
    assert result == 5, f"Expected 5, but got {result}"
    print("test_sqrt_function passed.")


test_sqrt_function()


# g
def test_sqrt_negative():
    with pytest.raises(ValueError, match="Cannot compute the square root of a negative number."):
        sqrt(-5)
    print("test_sqrt_negative passed.")


# h and i
def test_factorial_function():
    result1 = factorial(4)
    assert result1 == 24, f"Expected 24, but got {result1}"
    result2 = factorial(5)
    assert result2 == 120, f"Expected 120, but got {result2}"
    print("All test_factorial_function tests passed.")


test_factorial_function()


# j
def test_factorial_negative_case():
    with pytest.raises(ValueError, match="Cannot compute the factorial of a negative number."):
        factorial(-3)
    print("test_factorial_negative_case passed.")
