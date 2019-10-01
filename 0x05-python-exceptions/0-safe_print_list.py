#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for rec in my_list:
        try:
            if counter < x:
                print("{}".format(rec), end="")
                counter += 1
        except():
            continue
    print("")
    return(counter)
