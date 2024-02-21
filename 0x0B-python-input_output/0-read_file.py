#!/usr/bin/python3
"""
module: 0-read_file
"""


def read_file(filename=""):
    """function that"""
    with open(filename) as file:
        content = file.read()
        print(content, end="")
