#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# extraer el numero negativo
if number < 0:
    newn = number % -10
# extraer el numero positivo
elif number >= 0:
    newn = number % 10
# si es mayor que 5
if newn > 5:
    print('Last digit of {:d} is {:d} '
          'and is greater than 5'.format(number, newn))
# si es igual a 0
elif newn == 0:
    print('Last digit of {:d} is {:d} '
          'and is 0'.format(number, newn))
# si es menor a 6
elif newn < 6:
    print('Last digit of {:d} is {:d} '
          'and is less than 6 and not 0'.format(number, newn))
