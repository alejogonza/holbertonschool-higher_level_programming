#!/usr/bin/python3
Square = __import__('6-square').Square


my_square = Square(3, (0, 1))
my_square.my_print()
print("--")

my_square = Square(3, (1, 1))
my_square.my_print()
print("--")

my_square = Square(5, (3, 2))
my_square.my_print()
print("--")
