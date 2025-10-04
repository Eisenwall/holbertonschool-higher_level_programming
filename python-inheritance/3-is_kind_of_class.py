#!/usr/bin/python3
"""Module that checks if an object is an instance of a class
or of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass"""
    return isinstance(obj, a_class)
