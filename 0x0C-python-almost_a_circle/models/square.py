#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        square = "[Square] "
        id = "({}) ".format(self.id)
        x_y = "{}/{} - ".format(self.x, self.y)
        w_h = "{}/{}".format(self.width, self.height)

        return square + id + x_y + w_h

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        rectan = "[Square] "
        id = "({}) ".format(self.id)
        x_y = "{}/{} - ".format(self.x, self.y)
        sizes = "{}".format(self.size)

        return rectan + id + x_y + sizes

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            atrib_lists = ['id', 'size', 'x', 'y']
            for counter in range(len(args)):
                if atrib_lists[counter] == 'size':
                    setattr(self, 'width', args[counter])
                    setattr(self, 'height', args[counter])
                else:
                    setattr(self, atrib_lists[counter], args[counter])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        atrib_lists = ['id', 'size', 'x', 'y']
        d_response = {}

        for key in atrib_lists:
            if key == 'size':
                d_response[key] = getattr(self, 'width')
            else:
                d_response[key] = getattr(self, key)

        return d_response
