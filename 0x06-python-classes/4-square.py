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
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):

        """ Returns the area of a square"""

        return (self.size * self.size)
