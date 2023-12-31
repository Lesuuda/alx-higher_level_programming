#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    You must use the with statement
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    Your function should overwrite the content of
    the file if it already exists.
    Returns:
         int: the number of characters written to the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
