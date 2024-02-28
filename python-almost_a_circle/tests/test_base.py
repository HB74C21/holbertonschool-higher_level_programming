import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):

        Base._Base__nb_objects = 0

    def test_id_is_None(self):

        b1 = Base()

        self.assertEqual(b1.id, 1)

    def test_id_is_negative(self):

        b1 = Base(-1)

        self.assertEqual(b1.id, -1)

    def test_id_is_string(self):

        b1 = Base("str")

        self.assertEqual(b1.id, "str")

    def test_id_is_a_type_str(self):

        b1 = Base(str)

        self.assertEqual(type(b1.id), type(str))

    def test_multiple(self):

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
