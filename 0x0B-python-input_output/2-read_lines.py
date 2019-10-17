#!/usr/bin/python3
"""
2-read_lines

"""


def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file and prints it to stdout

    """
    linecount = 0
    with open(filename, "r", encoding='utf-8') as my_file:
        if nb_lines <= 0:
            print(my_file.read(), end="")
        else:
            for line in my_file:
                if linecount < nb_lines:
                    print(line, end="")
                    linecount += 1
