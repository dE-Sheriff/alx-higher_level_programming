#!/usr/bin/python3
"""
Module: 1-square
Defines a Square of size: size
"""


class Square(object):
    """
    This is a simple Square class
    """
    def __init__(self, size=0):
        """
        Initialize a sq. of size

        Args:
            size: Description of `size' default to 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
