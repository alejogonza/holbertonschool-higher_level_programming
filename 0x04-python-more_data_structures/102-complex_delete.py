#!/usr/bin/python3
def complex_delete(my_dict, value):
    mark = []
    for key in my_dict:
        if my_dict[key] == value:
            mark.append(key)
    for delet in mark:
        del my_dict[delet]
    return (my_dict)
