#!/usr/bin/python3
""" Defines a square based on 1-square.py"""

class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """__init__ instatiation
        Attributes:
                  size(int): size of the new square"""
        self.size = size

    @property
    def size(self):
        """get the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the area of a square"""
        return self.size * self.size

    def my_print(self):
        """prints # for area"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)

