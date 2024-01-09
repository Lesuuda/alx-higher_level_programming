#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value, raising TypeError or ValueError
        if conditions are not met
        """
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
