#!/usr/bin/python3
""" Find highest integer in list_of_integers """


def find_peak(list_of_integers):
    if list_of_integers is None:
        return float('-inf')
    max = list_of_integers[0]
    for i in list_of_integers:
        if max < i:
            max = i
    return max
