#!/usr/bin/python3
"""
This script defines a base class called BaseGeometry.
"""


class BaseGeometry:
    """
    Initializes a new instance of the BaseGeometry class.
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
