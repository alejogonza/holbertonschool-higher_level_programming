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

    def __str__(self):
        """ str meth """
        square = "[Square] "
        p_id = "({}) ".format(self.id)
        p_w_h = "{}/{}".format(self.width, self.height)
        p_x_y = "{}/{} - ".format(self.x, self.y)

        return square + p_id + p_x_y + p_w_h

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
        """ str meth """
        rectan = "[Square] "
        p_id = "({}) ".format(self.id)
        p_x_y = "{}/{} - ".format(self.x, self.y)
        p_sizes = "{}".format(self.size)

        return rectan + p_id + p_x_y + p_sizes

    def update(self, *args, **kwargs):
            """ update meth """
        if args is not None and len(args) is not 0:
            attb_lst = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attb_lst[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attb_lst[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return dict """
        attb_lst = ['id', 'size', 'x', 'y']
        res_dicc = {}

        for key in attb_lst:
            if key == 'size':
                res_dicc[key] = getattr(self, 'width')
            else:
                res_dicc[key] = getattr(self, key)

        return res_dicc
