#!/usr/bin/python3
""" 
class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        p_square = "[Square] "
        p_id = "({}) ".format(self.id)
        p_x_y = "{}/{} - ".format(self.x, self.y)
        p_w_h = "{}/{}".format(self.width, self.height)

        return p_square + p_id + p_x_y + p_w_h

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        p_rectangle = "[Square] "
        p_id = "({}) ".format(self.id)
        p_x_y = "{}/{} - ".format(self.x, self.y)
        p_sizes = "{}".format(self.size)

        return p_rectangle + p_id + p_x_y + p_sizes

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            attrib_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attrib_list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attrib_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        attrib_lst = ['id', 'size', 'x', 'y']
        dictin_response = {}

        for key in attrib_lst:
            if key == 'size':
                dictin_response[key] = getattr(self, 'width')
            else:
                dictin_response[key] = getattr(self, key)

        return dictin_response
