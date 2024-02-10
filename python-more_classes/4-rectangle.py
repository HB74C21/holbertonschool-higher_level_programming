#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

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
        if self.height < 0:
            raise ValueError("height must be >= 0")

    def perimeter(self):
        perimeter = (self.__height + self.__width) * 2

        if self.__height == 0 or self.__width == 0:
            perimeter = 0

        return perimeter

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

        return rectangle_str.strip("\n")

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def area(self):
        return self.__height * self.__width
