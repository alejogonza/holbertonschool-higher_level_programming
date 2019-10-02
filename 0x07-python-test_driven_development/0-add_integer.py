#!/usr/bin/python3
"""

The module function: add_integer().

make test: python3 -m doctest -v ./tests/0-add_integer.txt

"""


def add_integer(a, b=98):
    """
    calculate the sum of two ints

    Args:
    a: int, if is float cast to integer
    b: int, if is float cast to integer

    Return:
    the sum or error
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a_int = int(a)
    b_int = int(b)
    sum = a_int + b_int
    return (sum)
