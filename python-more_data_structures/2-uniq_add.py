#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (each integer only once).
    """
    unique_set = set(my_list)
    return sum(unique_set)
