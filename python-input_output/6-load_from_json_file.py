#!/usr/bin/python3
"""Function that creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        object: Python object (dict, list, etc.) represented in the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
