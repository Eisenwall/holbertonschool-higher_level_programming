#!/usr/bin/env python3
"""
Module defining VerboseList that extends Python's list class
and prints messages on modifications
"""


class VerboseList(list):
    """A list subclass that prints notifications on modifications"""

    def append(self, item):
        """Add an item and print a message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list with items and print a message"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and print a message"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Pop an item and print a message"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
