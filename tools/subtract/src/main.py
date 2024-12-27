def subtract(a: int, b: int) -> int:
    """Subtracts b from a.

    Args:
        a: first int
        b: second int

    Returns:
        int: The difference of a and b

    Raises:
        TypeError: If a or b are not integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a - b