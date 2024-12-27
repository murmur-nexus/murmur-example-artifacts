import pytest
from src.main import subtract

def test_subtract_positive_numbers():
    """Test subtraction with positive numbers"""
    assert subtract(5, 3) == 2
    assert subtract(10, 5) == 5
    assert subtract(100, 1) == 99

def test_subtract_negative_numbers():
    """Test subtraction with negative numbers"""
    assert subtract(-5, -3) == -2
    assert subtract(-10, -5) == -5

def test_subtract_mixed_numbers():
    """Test subtraction with mixed positive and negative numbers"""
    assert subtract(5, -3) == 8
    assert subtract(-5, 3) == -8
    assert subtract(0, -5) == 5
    assert subtract(-5, 0) == -5

def test_subtract_zero():
    """Test subtraction with zero"""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0

def test_subtract_invalid_types():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        subtract("5", 3)
    
    with pytest.raises(TypeError):
        subtract(5, "3")
    
    with pytest.raises(TypeError):
        subtract(5.5, 3)
    
    with pytest.raises(TypeError):
        subtract(5, 3.5)
