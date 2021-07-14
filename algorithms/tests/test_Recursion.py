import pytest
from Recursion import fac, power


@pytest.mark.parametrize('test_value, expected', [
    (5, 120), (25, 15511210043330985984000000), (10, 3628800)
])
def test_fac(test_value, expected):
    assert fac(test_value) == expected


@pytest.mark.parametrize('num, pow, expected', [
    (2, 5, 32), (3, 2, 9), (11, 2, 121)
])
def test_power(num, pow, expected):
    assert power(num, pow) == expected
