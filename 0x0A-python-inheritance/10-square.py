#!/usr/bin/python3
"""
10-square

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits class from Rectangle

    """

    def __init__(self, size):
        """
        p inst
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.size, self.size)

    def area(self):

        return super().area()
