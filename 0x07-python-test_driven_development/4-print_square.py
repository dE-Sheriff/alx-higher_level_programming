#!/usr/bin/python3
"""
Module: "4-print_square"
"""


def print_square(size):
    """A function that prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
