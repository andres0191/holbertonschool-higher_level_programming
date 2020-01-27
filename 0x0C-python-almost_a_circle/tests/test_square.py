#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
   def test_id(self):
       S1 = Square(1)
       S2 = Square(1, 2)
       S3 = Square(1, 2, 3)
       S4 = Square(1, 2, 3, 4)
       self.assertEqual(S2.x, 2)
       self.assertEqual(S3.y, 3)
       self.assertEqual(S4.id, 4)
​
   def test_ValueError(self):
       Base._Base__nb_objects = 0
       with self.assertRaisesRegex(ValueError, "width must be > 0"):
           Square(-2)
           Square(0)
       with self.assertRaisesRegex(ValueError, "x must be >= 0"):
           Square(10, -3)
       with self.assertRaisesRegex(ValueError, "y must be >= 0"):
           Square(10, 14, -5)
​
   def test_TypeError(self):
       Base._Base__nb_objects = 0
       with self.assertRaisesRegex(TypeError, "width must be an integer"):
           Square("22")
           Square(True)
       with self.assertRaisesRegex(TypeError, "x must be an integer"):
           Square(10, "yup")
           Square(10, True)
​
       with self.assertRaisesRegex(TypeError, "y must be an integer"):
           Square(10, 11, "hi")
           Square(10, 15, False)
​
   def test_str(self):
​
       Base._Base__nb_objects = 0
       S1 = Square(3)
       S2 = Square(3, 4)
       S3 = Square(3, 4, 5)
       self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 3")
       self.assertEqual(S2.__str__(), "[Square] (2) 4/0 - 3")
       self.assertEqual(S3.__str__(), "[Square] (3) 4/5 - 3")

    """task 11"""

    def test_getter(self):
        r1 = Square(5)
        self.assertEqual(r1.size, 5)

    def test_setter(self):
        r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)

    def test_string(self):
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = "Hi"

    def test_negative(self):
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = -5

    def test_zero(self):
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = 0

    def test_zero(self):
        r1 = Square(6)
        with self.assertRaises(TypeError):
            r1.size = 1.5

    def test_tupla(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = (2, 8)

    def test_empty(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = ""

    def test_none(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = None

    def test_list(self):
        r1 = Square(4)
        with self.assertRaises(TypeError):
            r1.size = [4, 7]

    def test_dict(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = {"hi": 5, "world": 8}

    def test_width(self):
        r1 = Square(6)
        r1.size = 6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)

    """ Task 12 """
    def test_update(self):
        s1 = 

if __name__ == "_main_":
    unittest.main()
