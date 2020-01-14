9#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def case1(self):
        a = __import__('6-max_integer').__doc__
        self.assertTrue(len(a) > 1)

    def test_float(self):
        self.assertEqual(max_integer([-3.23, 23.43, 44.2]), 44.2)

    def test_string_list(self):
        with self.assertRaises(TypeError):
            max_integer('hello', 'there')

    def test_string(self):
        self.assertEqual(max_integer("hello"), 'o')

    def test_valid(self):
        self.assertEqual(max_integer([-4, 4, 1, 0, 10, 1200]), 1200)

    def valid_tests(self):
        self.assertEqual(max_integer([0, 25, 55, 98]), 98)
        self.assertEqual(max_integer([1, 2, 98, 3]), 98)

    def negatives(self):
        self.assertEqual(max_integer([-98, -55, -20, -1]), -1)
        self.assertEqual(max_integer([-1, -2, -98, 3]), 3)

    def strings(self):
        self.assertEqual(max_integer("hello"), 'o')
