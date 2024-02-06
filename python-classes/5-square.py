#!/usr/bin/python3
""" This script defines the Square class, which represents a square """


class Square:
    """ This class represents a square """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    def area(self):
        return self.__size * self.__size
