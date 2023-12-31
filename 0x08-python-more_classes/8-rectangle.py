#!/usr/bin/python3
"""Defines an empty class"""


class Rectangle:
    '''an empty class that defines a rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instatiation
        Attributes:
                  height(int): height of rectangle
                  width(int): width of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return "Rectangle({}, {}".format(self.width, self.height)

    def __del__(self):
        """prints a message during deletion"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
        param rect_1: rectangle 1
        param rect_2: rectangle 2
        return: return the biggest rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        return rect_1 if area_1 >= area_2 else rect_2
