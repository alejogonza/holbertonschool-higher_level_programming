#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
try:
    print("1:",add_integer(-2, 4))
except Exception as e:
    print(e)
try:
    print("2:",add_integer(5.0, -4.8))
except Exception as e:
    print(e)
try:
    print("3:",add_integer(1,7,1))
except Exception as e:
    print(e)
try:
    print("4:",add_integer(2))
except Exception as e:
    print(e)
try:
    print("5:",add_integer(None))
except Exception as e:
    print(e)
try:
    print("6:",add_integer('2', 2))
except Exception as e:
    print(e)
try:
    print("7:",add_integer(2, '2'))
except Exception as e:
    print(e)
try:
    print("8:",add_integer(5, 5.0))
except Exception as e:
    print(e)
try:
    print("9:",add_integer(5.0, 5))
except Exception as e:
    print(e)
try:
    print("10:",add_integer(True, 2))
except Exception as e:
    print(e)
try:
    print("11:",add_integer(False, True))
except Exception as e:
    print(e)
try:
    print("12:",add_integer([1,2,3],4))
except Exception as e:
    print(e)
try:
    print("13:",add_integer(1,999999999999))
except Exception as e:
    print(e)
try:
    print("14:",add_integer())
except Exception as e:
    print(e)
