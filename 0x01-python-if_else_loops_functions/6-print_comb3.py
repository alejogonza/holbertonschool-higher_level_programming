#!/usr/bin/python3
for conv in range(0, 10):
    for rang in range(conv + 1, 10):
        if conv != rang:
            print('{}'.format(conv), end='')
            if conv == 8:
                print('{}'.format(rang))
            else:
                print('{:d}, '.format(rang), end='')
