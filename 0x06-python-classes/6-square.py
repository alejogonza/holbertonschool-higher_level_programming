#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for f1 in range(self.position[1]):
                print()
            for f2 in range(0, self.size):
                for k1 in range(self.position[0]):
                    print(" ", end='')
                for k2 in range(self.size):
                    print("#", end='')
                print()
