import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):

        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_width_setter(self):

        r = Rectangle(5, 10, 2, 3, 1)
        r.width = 8
        self.assertEqual(r.width, 8)

    def test_height_setter(self):

        r = Rectangle(5, 10, 2, 3, 1)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_x_setter(self):

        r = Rectangle(5, 10, 2, 3, 1)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_y_setter(self):

        r = Rectangle(5, 10, 2, 3, 1)
        r.y = 5
        self.assertEqual(r.y, 5)


if __name__ == '__main__':
    unittest.main()
