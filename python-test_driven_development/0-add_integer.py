#!/usr/bin/python3
"""
This script defines a function named add_integer that adds two numbers.
It ensures that both input parameters are integers or floats and converts
them to integers if necessary before performing the addition.
"""


def add_integer(a, b=98):
    """
    This function takes two parameters, a and b, and adds them together.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
