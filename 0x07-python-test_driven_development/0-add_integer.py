#!/usr/bin/python3
def add_integer(a, b=98):
    if a is None or type(a) is list:
        raise TypeError("a must be an integer")
    if b is None or type(b) is list:
        raise TypeError("b must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is list:
        raise TypeError("a must be an integer")
    if type(b) is list:
        raise TypeError("b must be an integer")
    return int(a + b)
