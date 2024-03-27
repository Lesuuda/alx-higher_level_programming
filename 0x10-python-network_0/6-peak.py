#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if list_of_integers == []:
        return None
    list_of_integers = sorted(list_of_integers)
    peak = list_of_integers[len(list_of_integers) - 1]
    return peak