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
        """Initialize the Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""

        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square object."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attribute of the square"""
        if len(args) > 0:
            attribut = ['id', 'size', 'x', 'y']
            for index, arg in zip(attribut, args):
                setattr(self, index, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
