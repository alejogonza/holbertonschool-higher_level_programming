#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            no_c = no_c + c
    return(no_c)
