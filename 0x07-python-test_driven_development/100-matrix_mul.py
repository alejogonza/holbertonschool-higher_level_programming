#!/usr/bin/python3
"""

The module function: matrix_mul().

make test: python3 -m doctest -v ./tests/100-matrix_mul.txt

"""


def matrix_mul(m_a, m_b):

    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for rec in m_a:
        if type(rec) is not list:
            raise TypeError('m_a must be a list of lists')
    for rec in m_b:
        if type(rec) is not list:
            raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    for rec in m_a:
        for elemt in rec:
            if type(elemt) is not int and type(elemt) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for rec in m_b:
        for elemt in rec:
            if type(elemt) is not int and type(elemt) is not float:
                raise TypeError('m_b should contain only integers or floats')

    for rec in m_a:
        if len(rec) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for rec in m_b:
        if len(rec) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    res = [[0 for reco in range(len(m_b[0]))] for ran in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
