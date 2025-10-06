#!/usr/bin/python3
"""
Integer validator module
Defines BaseGeometry class for geometry-related validation
"""


class BaseGeometry:
    """Class with basic geometry validation methods"""

    def area(self):
        """Raises an exception when called (not implemented yet)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than zero

        Args:
            name (str): the name of the variable
            value (any): the value to check

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
