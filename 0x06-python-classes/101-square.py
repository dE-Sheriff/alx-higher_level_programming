#!/usr/bin/python3
"""
Module 101-square
Defines class Square
Can access and update size and position
Can print to stdout the square using #'s
"""


class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Attributes:
            size: the size of the square `object'
            position: tuple of two positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square as the provided `value'

        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position as the provided `value'
        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) == tuple and len(value) == 2 and \
           type(value[0]) == int and type(value[1]) == int and \
           value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates and returns the area of the square
        """
        size = self.__size
        return size * size

    def my_print(self):
        print(self.__str__())

    def __str__(self):
        """
        String representation of square so call to print works
        """
        s = ""
        if self.__size == 0:
            return s

        s += "\n" * self.position[1]
        s += "\n".join([" " * self.__position[0] +
                        "#" * self.__size
                        for r in range(self.__size)])
        return s
