#!/usr/bin/python3
""" Defines a square based on 1-square.py"""


class Square:
    """Defines a square class"""
    def __init__(self, size=0):
        """__init__ instatiation
        Attributes:
                  size(int): size of the new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """ Returns the area of a square"""

        area = (self.__size * self.__size)
        return area
