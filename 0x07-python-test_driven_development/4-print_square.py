#!/usr/bin/python3

"""

The module function: print_square().

make test: python3 -m doctest -v ./tests/4-print_square.txt

"""


def print_square(size):
    """
    Function to print a square

    Args:
    size: The length of the square
    """
    interr = "size must be an integer"
    lesszeroerr = "size must be >= 0"

    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError(interr)
    if size < 0:
        raise ValueError(lesszeroerr)
    if size == 0:
        return
    else:
        print('\n'.join(['#' * size for j in range(size)]))
