#!/usr/bin/python3
"""class rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """a class rectnagle that inherits from the base class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation method.
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectngale
            x=0(int)
            y=0(int)
            id=none: this parameter is inherited from base
            """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        self.__height = value

    @property
    def x(self):
        """getter method for x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x value"""
        self.__x = value

    @property
    def y(self):
        """getter method for y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y value"""
        self.__y = value
