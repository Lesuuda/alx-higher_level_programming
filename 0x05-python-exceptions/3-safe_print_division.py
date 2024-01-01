#!/usr/bin/python3


def safe_print_division(a, b):

    """
    function that divides 2 integers and prints the result.
    """

    try:
        result = a / b
    except (ZeroDivisionError):
        result = None
    except Exception as e:
        result = None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))
