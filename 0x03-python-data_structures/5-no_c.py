#!/usr/bin/python3


def no_c(my_string):
    """removes 'c' and 'C' from a string"""

    result = ''
    for char in my_string:
        if char.lower() not in {'c'}:
            result += char
    return result
