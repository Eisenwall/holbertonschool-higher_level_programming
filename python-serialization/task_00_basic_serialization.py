#!/usr/bin/env python3
"""Basic serialization module: serialize a Python dictionary to a JSON file
and deserialize a JSON file back to a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file

    Args:
        data (dict): The Python dictionary to serialize
        filename (str): The output JSON filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file

    Args:
        filename (str): The JSON file to read

    Returns:
        dict: The deserialized Python dictionary
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
