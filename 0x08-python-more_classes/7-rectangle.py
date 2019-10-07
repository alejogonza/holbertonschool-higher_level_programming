#!/usr/bin/python3


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def height(self):

        return (self.__height)

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):

        return (self.__width)

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        a = self.__height * self.__width
        return (a)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        p = (self.__height * 2) + (self.__width * 2)
        return (p)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            ph = self.__height
            pw = self.__width
            string = ''.join((format(self.print_symbol) * pw + '\n') * ph)
            string = string[0:-1]
            return (string)

    def __repr__(self):
        return("Rectangle ({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
