#!/usr/bin/python3
def print_square(self, size=0):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for j in range(size):
       print("#", end="")
    print()
