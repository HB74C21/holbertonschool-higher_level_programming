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
        Initialize a Rectanglere with size
        """

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns a string representation a square.
        """
        return self.__size * self.__size
