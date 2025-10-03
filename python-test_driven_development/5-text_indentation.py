#!/usr/bin/python3
"""Module that prints a text with 2 new lines after each '.', '?', and ':'"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
