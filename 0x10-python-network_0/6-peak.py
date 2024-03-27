#!/usr/bin/python3
"""returns the peak value in an array"""


def find_peak(list_of_integers):
    """returns the peak value in an array"""
    if list_of_integers == []:
        return None
    list_of_integers = sorted(list_of_integers)
    peak = list_of_integers[len(list_of_integers) - 1]
    return peak
