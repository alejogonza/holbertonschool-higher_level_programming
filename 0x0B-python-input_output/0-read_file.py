#!/usr/bin/python3
"""
 0-read_file

"""


def read_file(filename=""):
    """
    a function that reads a text file and prints
    """
    with open(filename, "r", encoding='utf-8') as my_file:
        print(my_file.read(), end="")
