#!/usr/bin/python3


def best_score(a_dictionary):

    """
    description: returns the biggest integre value in a dictionary
    Parameters: a_dictionary, a dictionary
    Returns: max integer
    """

    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
