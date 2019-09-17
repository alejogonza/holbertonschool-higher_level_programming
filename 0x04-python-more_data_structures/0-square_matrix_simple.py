#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    if matrix == []:
        return(None)
    for rec in matrix:
        b = []
        for num in rec:
            b.append(num * num)
        a.append(b)
    return (a)
