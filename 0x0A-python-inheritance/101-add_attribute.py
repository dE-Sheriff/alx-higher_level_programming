#!/usr/bin/python3
"""A function that adds a new attribute to an object"""


def add_attribute(obj, name, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
