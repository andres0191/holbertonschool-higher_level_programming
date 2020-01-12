#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def case1(self):
        a = __import__('6-max_integer').__doc__
        self.assertTrue(len(a) > 1)
