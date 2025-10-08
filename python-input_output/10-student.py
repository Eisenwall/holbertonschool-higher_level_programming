#!/usr/bin/python3
"""Module that defines a Student class with a to_json method"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student

        If attrs is a list of strings, only include those attributes
        that exist in the instance.
        """
        if attrs is None:
            return self.__dict__.copy()
        return {k: v for k, v in self.__dict__.items() if k in attrs}
