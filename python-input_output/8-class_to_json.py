#!/usr/bin/python3
"""Function that returns the dictionary description with simple
data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Return a dictionary representation of an object for JSON serialization

    Only includes attributes that are serializable: list, dict, str, int, bool
    """
    return obj.__dict__.copy()
