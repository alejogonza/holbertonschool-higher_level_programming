#!/usr/bin/python3
"""
Class Base Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    rep
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        load init
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        getter width
        """
        return self.__width

    @property
    def height(self):
        """
        getter height
        """
        return self.__height

    @property
    def x(self):
        """
        getter x
        """
        return self.__x

    @property
    def y(self):
        """
        getter y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        set width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calc area
        """
        return self.__width * self.__height

    def display(self):
        """
        print rectangle
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """
     rep rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """
        update attrib
        """
        if (len(kwargs) > 0):
            if (kwargs.get('id') is not None):
                super().__init__(kwargs.get('id'))
            if (kwargs.get('width') is not None):
                self.width = kwargs.get('width')
            if (kwargs.get('height') is not None):
                self.height = kwargs.get('height')
            if (kwargs.get('x') is not None):
                self.x = kwargs.get('x')
            if (kwargs.get('y') is not None):
                self.y = kwargs.get('y')
        elif (len(args) > 0):
            for i in range(len(args)):
                if i == 0:
                    super().__init__(args[0])
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

    def to_dictionary(self):
        """
        dictionary about Rectangle
        """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
