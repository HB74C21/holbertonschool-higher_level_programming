#!/usr/bin/python3
"""
This script defines a function inherits_from that checks
if an object inherits from a given class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a given class
    """
    return issubclass(obj, a_class) and type(obj) is not a_class
