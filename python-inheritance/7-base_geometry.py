#!/usr/bin/python3
"""
This script defines a base class called BaseGeometry.
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.
    """

    def __init__(self):
        pass

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

    def area(self):
        raise Exception("area() is not implemented")
