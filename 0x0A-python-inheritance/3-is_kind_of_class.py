#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class.


    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is an instance or inherited instanceof a_class - True.
        otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
