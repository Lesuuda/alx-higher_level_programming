#!/usr/bin/pyrhon3


def only_diff_elements(set_1, set_2):

    """
    returns all elements present in only one set
    """

    one_set = set()
    for element in set_1:
        if element not in set_2:
            one_set.add(element)
    for element in set_2:
        if element not in set_1:
            one_set.add(element)
    return one_set
