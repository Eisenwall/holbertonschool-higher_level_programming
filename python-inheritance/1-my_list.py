#!/usr/bin/python3
"""Module that defines MyList class inheriting from list"""


class MyList(list):
    """MyList class inherits from list"""

    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
