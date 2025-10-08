#!/usr/bin/python3
"""Function that reads a text file (UTF-8) and prints it to stdout"""

def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
