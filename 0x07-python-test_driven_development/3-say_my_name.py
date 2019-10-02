#!/usr/bin/python3
"""

The module function: say_my_name().

make test: python3 -m doctest -v ./tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Function to prints full name

    Args:
    first_name: str
    last_name:  str
    """
    errtypefirst = "first_name must be a string"
    errtypelast = "last_name must be a string"

    if not isinstance(first_name, str):
        raise TypeError(errtypefirst)

    if not isinstance(last_name, str):
        raise TypeError(errtypelast)
    else:
        print("{:s} {:s} {:s}".format("My name is", first_name, last_name))
