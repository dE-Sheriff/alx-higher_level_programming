#!/usr/bin/python3
"""
The Rectangle module

This module provides the Rectangle object
"""


class Rectangle(object):
    """ A Rectangle with attributes width and height """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        s = ""
        if self.height == 0 or self.width == 0:
            return s
        for i in range(self.height):
            try:
                s += (str(self.print_symbol) * self.width)
            except Exception:
                s += (str(self.__class__.print_symbol) * self.width)
            if i is not self.height - 1:
                s += "\n"
        return s

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
