#!/usr/bin/python3
class Rectangle():
    """class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        if type(width) is not int and type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0 or height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

        @property
        def width(self):
            return (self.__width)

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            return (self.__height)

        @width.setter
        def height(self, value):
            self.__height = value

        def area(self):
            return (self.__width * self.__height)

        def perimeter(self):
            if widht == 0 or height == 0:
                return (0)
            else:
                return ((self.__width + self.__height) * 2)
