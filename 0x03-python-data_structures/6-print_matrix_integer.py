#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == "":
        print()
    for nums in matrix:
        for a, b in enumerate(nums):
            if a < (len(nums) - 1):
                print('{:d}'.format(b), end=" ")
            else:
                print('{:d}'.format(b), end="")
        print()
