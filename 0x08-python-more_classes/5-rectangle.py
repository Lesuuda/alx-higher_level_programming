#!/usr/bin/python3
"""Defines an empty class"""


class Rectangle:
    '''an empty class that defines a rectangle'''
    def __init__(self, width=0, height=0):
        """instatiation
        Attributes:
                  height(int): height of rectangle
                  width(int): width of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance attribute width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets the rectangle area"""

        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""

        perimeter = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            perimeter == 0
        return perimeter

    def __str__(self):
        """returns a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a message during deletion"""

        print("Bye rectangle...")
