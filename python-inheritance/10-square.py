#!/usr/bin/python3
"""
This script defines the Square class, which represents a square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Rectangle instance with given width and height.
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns a string representation of the rectangle.
        """
        return self.__size ** 2
