#!/usr/bin/env python3
"""Module demonstrating serialization and deserialization of custom
Python objects using pickle
"""

import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """Serialize the current instance to the given filename

        Args:
            filename (str): The file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file

        Args:
            filename (str): The file to load the object from

        Returns:
            CustomObject or None: The deserialized object or None on error
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError):
            return None
