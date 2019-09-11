#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    allnums = len(sys.argv)
    sum = 0
    for pos in range(1, allnums):
        nums = int(sys.argv[pos])
        sum = nums + sum
    print(sum)
