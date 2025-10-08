#!/usr/bin/python3
"""Function that returns the dictionary description of a class for JSON serialization"""


def class_to_json(obj):
    """
    Returns a dictionary with simple data structures (list, dict, str, int, bool)
    representing the attributes of an object.

    Args:
        obj (object): Instance of a class.

    Returns:
        dict: Dictionary representation of the object's attributes.
    """
    return obj.__dict__.copy()
