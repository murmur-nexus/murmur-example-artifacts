def multiply(a: int, b: int) -> int:
    """Multiplies a by b.

    Args:
        a: first int
        b: second int

    Returns:
        int: The product of a and b

    Raises:
        TypeError: If a or b are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a * b