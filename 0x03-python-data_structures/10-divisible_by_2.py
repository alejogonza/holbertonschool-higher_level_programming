#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = []
    n = None
    if my_list != n:
        for reco in my_list:
            if (reco % 2) == 0:
                div.append(True)
            else:
                div.append(False)
            return(div)