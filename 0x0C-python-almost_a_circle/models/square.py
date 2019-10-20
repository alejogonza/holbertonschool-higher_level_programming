#!/usr/bin/python3
"""
subclass Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    load init
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
         rep the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """
        update attrib
        """
        if (len(kwargs) > 0):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        elif (len(args) > 0):
            if (kwargs.get('id') is not None):
                super().__init__(kwargs.get('id'))
            if (kwargs.get('size') is not None):
                self.size = kwargs.get('size')
            if (kwargs.get('x') is not None):
                self.x = kwargs.get('x')
            if (kwargs.get('y') is not None):
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        dictionary
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
