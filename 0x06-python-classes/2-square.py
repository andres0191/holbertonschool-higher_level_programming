#!/usr/bin/python3
class Square:
    """"class Square defines a square by:
        private instance atribute size,
        and instantiation whit size
    """
    def __init__(self, size=0):
        """the paramethers of input
           are size, that is crucial
           for a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
