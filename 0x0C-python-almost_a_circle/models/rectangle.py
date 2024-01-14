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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """method to display rectangle instance with character #"""
        if self.width == 0 or self.height == 0:
            print("")
        for _ in range(self.height):
            print('#' * self.width)

    def __str__(self):
        """
        __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (
                f"[Rectangle] ({self.id})"
                f" {self.x}/{self.y} - {self.width}/{self.height}"
            )
