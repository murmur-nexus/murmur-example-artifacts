import pytest
from src.main import divide

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0
    assert divide(15, 3) == 5.0
    assert divide(1, 1) == 1.0

def test_divide_negative_numbers():
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0

def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_invalid_type():
    with pytest.raises(TypeError):
        divide("10", 2)
    with pytest.raises(TypeError):
        divide(10, "2")
    with pytest.raises(TypeError):
        divide(10.5, 2)
