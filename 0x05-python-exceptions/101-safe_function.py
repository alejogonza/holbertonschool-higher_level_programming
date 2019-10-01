#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except (IndexError, ZeroDivisionError, TypeError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    return (res)
