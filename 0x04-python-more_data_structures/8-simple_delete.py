#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):

    """
    deletes a key in a dictionary
    returns nothing
    """

    if key in a_dictionary:
        del a_dictionary[key]
