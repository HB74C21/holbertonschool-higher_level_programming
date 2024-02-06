#!/usr/bin/python3
""" This script defines the Square class, which represents a square """


class Square:
    """ This class represents a square """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not tuple(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        for i in range(self.position[1]):
            if self.position[1] > 0:
                print()
        for i in range(self.__size):
            if self.__size == 0:
                print()
            else:
                print(" " * self.position[0] + "#" * self.__size)

    def area(self):
        return self.__size * self.__size
