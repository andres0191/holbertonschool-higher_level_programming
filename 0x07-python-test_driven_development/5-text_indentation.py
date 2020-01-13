#!/usr/bin/python3

"""
    functino that prints a text
    whit 2 new lines aftesr each
    of these characters: '.', '?',
    and ':'.
"""


def text_indentation(text):
    """
    function that limit a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        flag = 0
        if text[i-1] == '.' or text[i-1] == '?' or text[i-1] == ':':
            print("\n")
        print(text[i], end="")
    print("\n")
