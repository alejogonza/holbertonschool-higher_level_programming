#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    delrep = set(my_list)
    for num in delrep:
        sum += num
    return (sum)
