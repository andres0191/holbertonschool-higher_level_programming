#!/usr/bin/python3
def print_square(self, size=0):
    if size is None:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float:
        raise TypeError("size must be an integer")
#    if size is < 0:
#        raise TypeError("size must be an integer")
#    if size is <= 0:
#        raise ValueError("size must be >= 0")
    return (size ** 2)

def area(self):
    return (self.__size ** 2)

@property
def size(self):
    return self.__size

@size.setter
def size(self, value):
    self.__size = value

def my_print(self):
    if self.__size == 0:
        print("\n", end="")
    else:
        for i in range(self.__size):
            x = "#" * self.__size
            print(x)
