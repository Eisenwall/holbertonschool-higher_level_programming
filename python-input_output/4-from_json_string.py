#!/usr/bin/python3
"""Function that returns an object represented by a JSON string"""

import json

def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to be converted.

    Returns:
        object: Python data structure (dict, list, etc.) represented by JSON.
    """
    return json.loads(my_str)
