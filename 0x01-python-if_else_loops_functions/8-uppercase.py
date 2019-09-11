#!/usr/bin/python3
def uppercase(str):
    for toupper in str:
        if ord(toupper) >= ord('a') and ord(toupper) <= ord('z'):
            toupper = chr(ord(toupper) - ord(' '))
        print('{:s}'.format(toupper), end='')
    print('\n', end='')
