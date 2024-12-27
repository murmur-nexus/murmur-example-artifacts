def divide(a: int, b: int) -> float:
    """Divides a by b.

    Args:
        a: first int
        b: second int

    Returns:
        float: The quotient of a and b

    Raises:
        TypeError: If a or b are not integers
        ZeroDivisionError: If b is zero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b