#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
    except:
        div = None
    finally:
        print("{:s} {}".format("Inside result:", div))
    return(div)
