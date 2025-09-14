#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    If the key exists, its value is replaced.
    If the key does not exist, it is added.
    """
    a_dictionary[key] = value
    return a_dictionary
