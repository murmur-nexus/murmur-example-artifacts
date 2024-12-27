import pytest
from src.main import add

def test_add_positive_numbers():
    """Test adding two positive integers."""
    assert add(1, 2) == 3
    assert add(10, 20) == 30
    assert add(100, 200) == 300

def test_add_negative_numbers():
    """Test adding negative integers."""
    assert add(-1, -2) == -3
    assert add(-10, -20) == -30
    assert add(-100, -200) == -300

def test_add_mixed_numbers():
    """Test adding positive and negative integers."""
    assert add(-1, 2) == 1
    assert add(10, -20) == -10
    assert add(-100, 200) == 100

def test_add_zero():
    """Test adding zero with positive and negative integers."""
    assert add(0, 0) == 0
    assert add(0, 10) == 10
    assert add(10, 0) == 10
    assert add(0, -10) == -10
    assert add(-10, 0) == -10

def test_add_type_error():
    """Test that TypeError is raised for non-integer inputs."""
    with pytest.raises(TypeError, match="Both arguments must be integers"):
        add(1.5, 2)
    
    with pytest.raises(TypeError, match="Both arguments must be integers"):
        add(1, "2")
    
    with pytest.raises(TypeError, match="Both arguments must be integers"):
        add("1", 2)
    
    with pytest.raises(TypeError, match="Both arguments must be integers"):
        add(None, 2)
