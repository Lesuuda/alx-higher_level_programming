#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """base class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
        Args:
            id=None(int) - if id is not None, assign the public instance
            attribute id with its argument value.
            otherwise increment __nb_objects and assign the new value
            to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
