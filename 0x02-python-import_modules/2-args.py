#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = (sys.argv)
    argslen = len(sys.argv)
    rest = argslen - 1
    if rest == 0:
        print("{:d} arguments.".format(rest))
    if rest == 1:
        print("{:d} argument:".format(rest))
        print("{:d}: {:s}".format(rest, args[1]))
    if rest > 1:
        print("{:d} arguments:".format(rest))
        for a in range(1, argslen):
            print("{:d}: {:s}".format(a, args[a]))
