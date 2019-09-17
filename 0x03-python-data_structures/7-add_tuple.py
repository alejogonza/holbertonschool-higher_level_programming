#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_tup = ()
    len_1 = len(tuple_a)
    len_2 = len(tuple_b)

    if len_1 == 0:
        tuple_a = (0, 0)
    elif len_1 == 1:
        tuple_a = tuple_a + (0, )

    if len_2 == 0:
        tuple_b = (0, 0)
    elif len_2 == 1:
        tuple_b = tuple_b + (0, )

    n_tup = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return(n_tup)
