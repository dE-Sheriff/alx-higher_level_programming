#!/usr/bin/python3
"""A function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if search_string in line:
                file.write(line)
                file.write(new_string)
            else:
                file.write(line)
