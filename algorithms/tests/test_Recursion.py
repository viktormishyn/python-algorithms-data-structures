import pytest
from Recursion import fac, power, find_in_array


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


@pytest.mark.parametrize('array, target, expected', [
    ([1, 3, 5, 77, 23], 23, True),
    ([1, 3, 5, 77, 23], 22, False),
    (['sss', 2, 4, 6, 8], 'sss', True),
    ([], 'sss', False),
])
def test_find_in_array(array, target, expected):
    assert find_in_array(array, target) == expected
