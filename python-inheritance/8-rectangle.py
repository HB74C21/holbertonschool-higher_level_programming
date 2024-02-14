#!/usr/bin/python3
"""
This script defines a base class called BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initializes a new instance of the BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Validates that the given value is an integer greater than zero.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
