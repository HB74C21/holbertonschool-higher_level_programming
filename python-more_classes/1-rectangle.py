#!/usr/bin/python3
""" Create a class Rectangle that defines a rectangle """


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Getter method for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")
