#!/usr/bin/python3
"""
Function that print a square with character #
size is the size length of the square
size must be an integer otherwise raise aTypeError
size must be greater than zero otherwise raise a ValueError
of soze is a float raiseaTyoeError
"""


def print_square(size):
    """prints a square with character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print('#' * size)
