#!/usr/bin/python3
def pascal_triangle(n):
    """
    return the pascal triangle

    """

    pas = []
    p = []

    for v in range(n):
        res_list = []
        varone = -1
        vartwo = 0
        for j in range(len(p) + 1):
            if varone == -1 or vartwo == len(p):
                res_list += [1]
            else:
                res_list += [p[varone] + p[vartwo]]
            varone += 1
            vartwo += 1
        pas.append(res_list)
        p = res_list[:]

    return pas
