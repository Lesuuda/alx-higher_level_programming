#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    """prints the contents of a list in reverse"""

    for num in reversed(my_list):
        if len(my_list) == 0:
            return None
        print("{:d}".format(num))
