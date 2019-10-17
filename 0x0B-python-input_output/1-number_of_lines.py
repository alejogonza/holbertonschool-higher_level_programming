#!/usr/bin/python3
"""
 1-number_of_lines

"""


def number_of_lines(filename=""):
    """
return the number of lines of a text file

    """
    linecount = 0
    with open(filename, "r", encoding='utf-8') as my_file:
        for line in my_file:
            linecount += 1
        return(linecount)
