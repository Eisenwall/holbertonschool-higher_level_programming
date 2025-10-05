#!/usr/bin/python3
"""Module defining MyList class"""

class MyList(list):
    """Custom list class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying it"""
        try:
            print(sorted(self))
        except TypeError:
            
            print(sorted(self, key=lambda x: str(x)))
