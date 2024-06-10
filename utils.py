"""
Module utils.

This module contains basic mathematical functions for demonstration purposes.
"""

def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Subtract one integer from another.

    Args:
        a (int): The integer to be subtracted from.
        b (int): The integer to subtract.

    Returns:
        int: The difference of a and b.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divide one integer by another.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
