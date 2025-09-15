#!/usr/bin/python3
"""
0. Integers addition
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers) and returns the result.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
