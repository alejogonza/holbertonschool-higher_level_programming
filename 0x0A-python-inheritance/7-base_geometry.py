#!/usr/bin/python3
"""
 7-base_geometry

"""


class BaseGeometry:
    """

    `def area(self)`
    `def integer_validator(self, name, value)`
    """

    def area(self):
        """
        public method to determine area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
