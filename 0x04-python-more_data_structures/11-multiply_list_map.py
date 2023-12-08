#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):

    """
    Description: multiplies using map
    Parameters: list and number to be multiplied with
    Returns: result of multiplication
    """

    return list(map(lambda x: x * number, my_list))
