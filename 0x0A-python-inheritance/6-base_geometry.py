#!/usr/bin/python3
"""
class BaseGeometry (based on 5-base_geometry.py).

Public instance method:
def area(self): that raises an Exception with the message area()
is not implemented
"""


class BaseGeometry:
    """A base class representing geometry."""

    def area(self):
        """raises an exception with a message area() is not implemented"""
        raise Exception("area() is not implemented")
