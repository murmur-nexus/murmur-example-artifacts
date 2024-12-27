import pytest
from src.main import multiply

def test_basic_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(4, 5) == 20
    assert multiply(1, 1) == 1

def test_multiply_with_zero():
    assert multiply(0, 5) == 0
    assert multiply(10, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_with_negative():
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6

def test_type_error():
    with pytest.raises(TypeError):
        multiply("2", 3)
    
    with pytest.raises(TypeError):
        multiply(2, "3")
    
    with pytest.raises(TypeError):
        multiply(2.5, 3)
    
    with pytest.raises(TypeError):
        multiply(2, 3.5)
