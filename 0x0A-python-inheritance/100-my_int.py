#!/usr/bin/python3
"""
classs MyInt tha inherits from int class and inverts == to !=
and vice versa
"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        """overides == to !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverts the behaviour of !="""
        return super().__eq__(other)
