#!/usr/bin/python3
"""
Module: 2-is_same_class
Checks object against a class"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of specified class """
    return type(obj) is a_class
