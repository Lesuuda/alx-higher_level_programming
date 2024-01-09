#!/usr/bin/python3
"""
Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


class BaseGeometry:
    """BaseGeometry class thainherits from Rectangle and calculates the area"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value, raising TypeError or
        ValueError if conditions are not met"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Returns a formal string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Istantiation  with size. if uses super() to inerit the parent"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Returns a formal string representation of the square"""
        return f"Square({self.__size})"
