#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return (None)
    if search > len(my_list):
        return (None)
    cplist = my_list.copy()
    s = search - 1
    cplist[s] = replace
    return(cplist)
