#!/usr/bin/python3
""" Class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Rectangle that heritance of class Base """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter of width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter of height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter of x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter of y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ print rectangle representate with # """
        r = ('\n' * self.y)
        for i in range(self.height):
            r += (' ' * self.x)
            r += ('#' * self.width + '\n')
        print(r, end="")

    def __str__(self):
        """ create a __str__ method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update the class rectangle by improving
            the public method
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary represtantion of
            a rectangle
        """
        dic = {}
        dic["x"] = self.__x
        dic["y"] = self.__y
        dic["id"] = self.id
        dic["height"] = self.height
        dic["width"] = self.width
        return (dic)
