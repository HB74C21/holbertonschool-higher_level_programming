#!/usr/bin/python3
"""
This script defines the Square class, which represents a square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square.
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
