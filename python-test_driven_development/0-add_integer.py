#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be integers or floats, otherwise raise a TypeError.
    Floats are casted to integers before addition.

    Args:
        a (int or float): first number
        b (int or float, optional): second number. Defaults to 98.

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
