#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys (alphabetically).
    Only sorts keys at the first level.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
