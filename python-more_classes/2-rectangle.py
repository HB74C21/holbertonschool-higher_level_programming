#!/usr/bin/python3
""" This module defines a Rectangle class """


class Rectangle:
    """ Represents a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        perimeter = (self.__height + self.__width) * 2

        if self.__width == 0 or self.__height == 0:
            perimeter = 0

        return perimeter

    def area(self):
        return self.__width * self.__height
