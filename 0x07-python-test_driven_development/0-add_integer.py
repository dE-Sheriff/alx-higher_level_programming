#!/usr/bin/python3
""" Module Test: Sample function that adds two numbers"""


def add_integer(a, b=98):
    """A simple function that adds two numbers"""
    if not type(a) in [float, int]:
        raise TypeError('a must be an integer')
    if not type(b) in [float, int]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
