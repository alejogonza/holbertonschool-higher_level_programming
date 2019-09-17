#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for rec in matrix:
        b = []
        for num in rec:
            a.append(num * num)
        b.append(a)
    return (b)
