#!/usr/bin/python3
"""Module containing print_sorted func"""


class MyList(list):
    """Class inherited from list class"""

    def print_sorted(self):
        """Method to print sorted list"""
        if issubclass(MyList, list):
        print(sorted(self))
