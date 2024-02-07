#!/usr/bin/python3
"""
Module: 6-square
Defines a Square of size: size
"""


class Square(object):
    """
    This is a simple Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a sq. of size

        Args:
            size: Description of `size' default to 0
            position: tuple of positive integers
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """
        Prints the square based on the size using `#'
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            hashes = [" " * self.__position[0] + "#" * self.__size
                      for i in range(self.__size)]
            print("\n".join(hashes))
        # for i in range(self.__size):
        #    for j in range(self.__size):
        #        print("#", end="")
        #    print()
        # print()

    @property
    def position(self):
        """
        Retrieve the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the Square
        Args:
            value: a tuple of 2 positive integers
        """
        if type(value) == tuple and len(value) == 2 and type(value[0]) == int \
                and type(value[1]) == int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
