#!/usr/bin/python3
"""
This script defines a function is_kind_of_class that checks
if an object is an instance of a given class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a given class or a subclass thereof.
    """
    return True if isinstance(obj, a_class) else False
