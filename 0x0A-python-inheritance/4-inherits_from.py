#!/usr/bin/python3
"""
Module: 4-inherits_from
Checks object against a class"""


def inherits_from(obj, a_class):
    """Method that return True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
