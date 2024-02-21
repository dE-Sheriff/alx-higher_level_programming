#!/usr/bin/python3
"""
module: 1-write_file
"""


def write_file(filename="", text=""):
    """function that writes data to file"""

    with open(filename, 'w') as file:
        return file.write(text)
