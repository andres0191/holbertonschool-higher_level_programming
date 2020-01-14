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
