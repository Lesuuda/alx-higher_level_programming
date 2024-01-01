#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    """prints a list by another list and returns the result
    """

    result_list = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i] if i < len(my_list_1) else 0
            elem_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not (
                    isinstance(elem_1, (int, float)) and
                    isinstance(elem_2, (int, float))
            ):
                raise TypeError("wrong type")
            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")
            result = elem_1 / elem_2
            result_list.append(result)
        except TypeError as e:
            print("wrong type")
            result_list.append(0)
        except ZeroDivisionError as e:
            print("division by 0")
            result_list.append(0)
        finally:
            pass
    return result_list
