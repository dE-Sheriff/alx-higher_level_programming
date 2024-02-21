#!/usr/bin/python3
"""
Module:
"""


def append_write(filename="", text=""):
    """function that """

    with open(filename, 'a') as file:
        return file.write(text)
