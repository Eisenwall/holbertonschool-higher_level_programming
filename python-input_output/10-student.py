#!/usr/bin/python3
"""Defines a Student class with JSON serialization capability"""

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    If None, return all attributes.

        Returns:
            dict: Dictionary of requested attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
