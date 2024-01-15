#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for the size of the square"""
        self.width = value
        self.height = value;

    def update(self, *args, **kwargs):
        """
        public method to update arguments
        Args:
            *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
            **kwargs can be thought of as a double pointer to a dictionary:
            key/value (keyworded arguments)
            **kwargs must be skipped if *args exists and is not empty
            Each key in this dictionary represents an attribute to
            the instance
        """

        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:

            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
                    
    def __str__(self):
        """return the print() and str() representation of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
