#!/usr/bin/python3
"""Module that prints a square with the character #"""


def print_square(size):
    """Prints a square of size `size` using # characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
