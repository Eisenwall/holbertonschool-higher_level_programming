#!/usr/bin/python3
"""Module that defines Square class inheriting from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square with private size"""
        self.integer_validator("size", size)
        self.__size = size
        # Call the parent Rectangle constructor
        # with width and height equal to size
        super().__init__(size, size)
