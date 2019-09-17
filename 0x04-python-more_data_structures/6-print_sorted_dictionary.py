#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sh = sorted(a_dictionary)
    for i in sh:
        print('{}: {}'.format(i, a_dictionary[i]))
