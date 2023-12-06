#!/usr/bin/python3


def search_replace(my_list, search, replace):

    """
    replaces an element of a list with a provided element
    """

    new_list = []
    for element in my_list:
        new_element = replace if element == search else element
        new_list.append(new_element)
    return new_list
