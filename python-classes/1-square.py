i#!/usr/bin/python3
"""Defines a Square with a private size."""


class Square:
    """Represents a square with a private attribute size."""

    def __init__(self, size):
        """Initialize the square with size (no validation)."""
        self.__size = size
