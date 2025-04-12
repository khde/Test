import pytest


@pytest.fixture
def number1():
    return 5


@pytest.fixture
def number2():
    return 12


def test_add(number1, number2):
    assert number1 + number2 ==  17


def test_sub(number1, number2):
    assert number1 - number2 == -7


def test_mul(number1, number2):
    assert number1 * number2 == 60


def test_mod(number1, number2):
    assert number1 % number2 == 5

