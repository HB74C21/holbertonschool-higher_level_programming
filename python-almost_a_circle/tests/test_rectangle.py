#!/usr/bin/python3
"""
Unittest for file rectangle.py.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class representing a test case for Rectangle class."""

    def test_constructor(self):
        """Test the constructor of Rectangle."""
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_width_setter(self):
        """Test the setter for width."""
        r = Rectangle(5, 10, 2, 3, 1)
        r.width = 8
        self.assertEqual(r.width, 8)

    def test_height_setter(self):
        """Test the setter for height."""
        r = Rectangle(5, 10, 2, 3, 1)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_x_setter(self):
        """Test the setter for x."""
        r = Rectangle(5, 10, 2, 3, 1)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_y_setter(self):
        """Test the setter for y."""
        r = Rectangle(5, 10, 2, 3, 1)
        r.y = 5
        self.assertEqual(r.y, 5)


if __name__ == '__main__':
    unittest.main()
