#!/usr/bin/python3
"""
    function that prints a
    square whit the character '#'
"""


def print_square(size):
    """
        cases of error and function
    """
    if type(size) is not int and type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
