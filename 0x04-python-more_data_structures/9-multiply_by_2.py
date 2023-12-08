#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    """
    multiplies all values by 2
    param: originial dictionary(a_dictionary)
    return: a new dictionary with value multiplied by two
    """

    multiplied_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return multiplied_dict
