#!/usr/bin/python3
"""
Module containing the Square class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square object with a given size, position, and ID."""
        self.size = size
        self.x = x
        self.y = y
        self.width = size
        self.height = size

        super().__init__(self.width, self.height, x, y, id)

    def __str__(self):
        """Return a string representation of the Square object."""
        return "[Square]({}) {}/{} - {}".format(self.id, self.x,
                                                self.y, self.size)
