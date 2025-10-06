#!/usr/bin/python3
"""Module providing BaseGeometry class for geometry operations."""


class BaseGeometry:
    """A base class for geometric calculations."""

    def area(self):
        """Method that must be implemented by subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Ensure the given value is a valid positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
