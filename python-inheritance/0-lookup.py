#!/usr/bin/python3
"""
Function that returns the list of available attribute and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    liste = dir(obj)
    return liste
