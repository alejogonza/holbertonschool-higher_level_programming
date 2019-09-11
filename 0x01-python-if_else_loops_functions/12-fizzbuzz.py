#!/usr/bin/python3
def fizzbuzz():
    for replace in range(1, 101):
        if replace % 3 == 0:
            print('Fizz', end='')
        if replace % 5 == 0:
            print('Buzz', end='')
        if replace % 3 != 0 and replace % 5 != 0:
            print('{:d}'.format(replace), end='')
        if replace == 101:
            print('\n', end='')
        else:
            print(' ', end='')
