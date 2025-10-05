#!/usr/bin/python3
"""Module defining MyList class"""


class MyList(list):
    """Custom list class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
