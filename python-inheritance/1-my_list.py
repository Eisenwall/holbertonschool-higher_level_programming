#!/usr/bin/python3
"""
Module that defines class MyList.
"""


class MyList(list):
    """
    Class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        if issubclass(MyList, list):
            print(sorted(self))
