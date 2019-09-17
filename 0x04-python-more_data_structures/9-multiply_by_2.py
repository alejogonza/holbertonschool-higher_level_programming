#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = {}
    for rec in a_dictionary:
        mul[rec] = a_dictionary[rec] * 2
    return (mul)
