#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """class definition that inherits from list"""

    def print_sorted(self):
        """prints the attributes in sorted form(ascending)"""

        sorted_list = sorted(self)
        return sorted_list
