#!/usr/bin/python3
class Test():
    pass
"""Function that add a two integer"""


def add_integer(a, b=89):
    """add two int"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    c = int(a)+int(b)
    return c
