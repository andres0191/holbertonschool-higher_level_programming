#!/usr/bin/python3
class Square:
    """"class Square defines a square by:
        private instance atribute size,
        and instantiation whit size
    """
    def __init__(self, size=0, position=0):
        """the paramethers of input
           are size, that is crucial
           for a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def position(self):
        return self.__position

    def position(self, value):

    def my_print(self):
       else:
            for i in range(self.__size):
                x = "#" * self.__size
                print(x, end="")
