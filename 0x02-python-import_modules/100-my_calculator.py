#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argnums = (sys.argv)
    lennums = len(sys.argv)
    rest = lennums - 1
    a = int(argnums[1])
    sign = argnums[2]
    b = int(argnums[3])
    if lennums != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argnums[2] == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, add(a,b)))
    elif argnums[2] == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, sub(a,b)))
    elif argnums[2] == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, mul(a,b)))
    elif argnums[2] == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, sign, b, div(a,b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
