#!/usr/bin/python3
def best_score(a_dictionary):
    k = ""
    m = 0
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > m:
            m = a_dictionary[key]
            k = key
    return (k)
