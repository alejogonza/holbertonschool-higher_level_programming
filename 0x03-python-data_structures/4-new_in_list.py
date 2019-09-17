#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if copy is None:
        return
    if idx < 0:
        return (copy)
    if idx > len(my_list) - 1:
        return (copy)
    for pos, re in enumerate(copy):
        copy[idx] = element
        return (copy)
