#!/usr/bin/python3
"""
Module: 4-square
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square
        with the given size
        """
        size = self.__size
        return size * size

    def __eq__(self, another):
        """
        Checks the equality of the squares
        """
        return self.size == another.size

    def __ne__(self, another):
        """
        checks the inequality (!=) of 2 squares
        beign compared
        """
        return self.size != another.size

    def __gt__(self, another):
        """
        compares 2 squares using the > operator
        """
        return self.size > another.size

    def __lt__(self, another):
        """
        compares 2 squares using the < check
        """
        return self.size < another.size

    def __ge__(self, another):
        """
        compares 2 squares using the >= operator
        """
        return self.size >= another.size

    def __le__(self, another):
        """
        compares 2 squares using the <= operator
        """
        return self.size <= another.size
