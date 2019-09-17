#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return (my_list)
    if search > len(my_list):
        return (my_list)
    pat = []
    for let in my_list:
        pat.append(let if let != search else replace)

    return (pat)
