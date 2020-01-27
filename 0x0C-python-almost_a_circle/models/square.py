#!/usr/bin/python3
""" Class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ call the super class with id- this super call
            with use the logic of the __init__ of the base class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ method __str__ """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """ getter of size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ setter of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Returns an instance with all atributes """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns the dictionary representation of a square """
        dic = {}
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        dic["id"] = self.id
        return (dic)
