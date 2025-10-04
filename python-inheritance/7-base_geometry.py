#!/usr/bin/python3
"""Module that defines BaseGeometry class with area() and integer_validator()"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
