#!/usr/bin/python3
""" This script defines the Square class, which represents a square """


class Square:
    """ This class represents a square """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
