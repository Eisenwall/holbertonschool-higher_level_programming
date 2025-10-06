#!/usr/bin/python3
"""
Module defining Square class inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""

    def __init__(self, size):
        """Initialize the square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
