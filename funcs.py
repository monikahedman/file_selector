"""
General file containing functions that are not class-specific.
"""


def equalize_lists(list1, list2):
    """
    Method takes in two lists and makes them equal. The first list, list1, is the one being modified. list1 is cleared
    and then all of the items in list2 are appeneded to list1.
    :param list1: The list to modify
    :param list2: The list containing the desired contents
    """
    clear_list(list1)
    for item in list2:
        list1.append(item)


def clear_list(lst):
    """
    Clears the list without setting it to a new one.
    :param lst: list to be altered.
    """
    lst[:] = []


def is_num(string):
    """
    Indicates if the given string is a number. Catches the ValueError thrown by the cast and returns false, as the
    string is not a number
    :param string: the string to check if number
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def str_to_bool(string):
    """
    Converts a string to a boolean. If the string is True or Yes, then True is returned. False is returned for any other
    value.
    :param string: string to look at
    :return: boolean value of the string
    """
    if string == "True" or string == "Yes":
        return True
    return False

