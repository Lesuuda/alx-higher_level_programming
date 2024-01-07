#!/usr/bin/python3
"""
A function that adds two numbers;
Attributes:
         a(int): first number
         b=98(int): second number
Raises: TypeError if one of the numbers is not an integer
Return: a + b
"""


def add_integer(a, b=98):
    """adds two number and returns the result"""

    a = int(a)
    b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an ineteger")
    return a + b
         
