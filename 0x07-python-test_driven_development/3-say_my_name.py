#!/usr/bin/python3
"""
    function that prints: My name
    is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    function and cases of error
    """
    if first_name is '\n' and last_name is '\n':
        print("My name is \n\n"
    if first_name is ' ' and last_name is ' ':
        print("My name is    ")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}\n".format(first_name, last_name), end="")
