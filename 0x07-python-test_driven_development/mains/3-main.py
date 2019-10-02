#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name


try:
  print("1",say_my_name("walter", "white"))
except Exception as e:
    print(e)

try:
  print("2",say_my_name("guero", None))
except Exception as e:
    print(e)

try:
  print("3",say_my_name(None, "mimi"))
except Exception as e:
    print(e)

try:
  print("4",say_my_name())
except Exception as e:
    print(e)

try:
  print("5",say_my_name(5, 6))
except Exception as e:
    print(e)

try:
  print("6",say_my_name(8, "tortas"))
except Exception as e:
    print(e)

try:
  print("7",say_my_name("de", 8))

except Exception as e:
    print(e)

try:
  print("8",say_my_name("guevito", ))
except Exception as e:
    print(e)
