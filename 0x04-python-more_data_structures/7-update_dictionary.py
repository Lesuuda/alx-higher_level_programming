#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):

    """
    updates the key value of a dictionary with a given value
    return nothing
    """

    if key in a_dictionary:
        a_dictionary[key] = value
