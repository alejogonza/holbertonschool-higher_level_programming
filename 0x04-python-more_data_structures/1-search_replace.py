#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cplist = my_list.copy()
    s = search - 1
    cplist[s] = replace
    return(cplist)
