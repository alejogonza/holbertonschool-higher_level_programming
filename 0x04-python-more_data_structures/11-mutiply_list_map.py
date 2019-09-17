#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    maps = map((lambda x: number * x), my_list)
    return(list(maps))
