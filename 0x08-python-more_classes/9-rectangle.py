#!/usr/bin/python3


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def area(self):

        return self.height * self.width

    def perimeter(self):

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):

        if self.width == 0 or self.height == 0:
            return ""
        rect = str(self.print_symbol) * self.width
        rect = (rect + "\n") * (self.height - 1) + rect
        return rect

    def __repr__(self):

        if self.width == 0 or self.height == 0:
            return {}
        return "Rectangle({}, {})".format(self.width, self. height)

    def __del__(self):

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()
