from CS506 import square
import pytest


def test_positive():
    assert square(2) == 4  # Assert checks if something is true if not the test will fail.
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
