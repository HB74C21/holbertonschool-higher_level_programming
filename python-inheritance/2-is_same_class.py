#!/usr/bin/python3
"""
This script defines a function is_same_class that checks
if an object belongs to the same class as another one.
"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to the same class as another one
    """
    return True if type(obj) is a_class else False
