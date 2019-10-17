#!/usr/bin/python3
"""
3-write_file

"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number of characters written

    """
    with open(filename, "w", encoding="utf-8") as my_file:
        charcount = my_file.write(text)
    return (charcount)
