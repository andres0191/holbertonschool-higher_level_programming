#!/usr/bin/python3
class test():
    def add_integer(a, b=89):
        try:
            a is not int or float
            raise TypeError("a must be an integer")
            b is not int or float
            raise TypeError("b must be an integer")
        except:
            return a+b
