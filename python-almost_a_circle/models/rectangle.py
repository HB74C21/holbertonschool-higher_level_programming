#!/usr/bin/python3
"""
Module containing the Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """
    Class representing a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value