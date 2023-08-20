#!/usr/bin/python3
import sys
if __name__ == "__mmain__":

    """print the number of and lists of arguments"""

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}:{}".format(i + 1, sys.argv[i + 1]))
