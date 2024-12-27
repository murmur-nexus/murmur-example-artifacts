import pytest
from src.main import is_prime

def test_prime_numbers():
    assert is_prime("2") == True
    assert is_prime("3") == True
    assert is_prime("17") == True
    assert is_prime("97") == True

def test_non_prime_numbers():
    assert is_prime("4") == False
    assert is_prime("15") == False
    assert is_prime("100") == False

def test_edge_cases():
    assert is_prime("1") == False  # 1 is not considered prime
    assert is_prime("0") == False
    assert is_prime("-7") == False  # Negative numbers aren't prime

def test_invalid_inputs():
    assert is_prime("abc") == False
    assert is_prime("12.34") == False
    assert is_prime("") == False
    assert is_prime(" ") == False