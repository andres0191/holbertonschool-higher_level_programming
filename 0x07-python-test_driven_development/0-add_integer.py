#!/usr/bin/python3
"""
    function that add two int
    if the variable not is int
    cast to int
"""


def add_integer(a, b=98):
    """
    function and cases of error
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
