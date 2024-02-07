#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """
    Initialize MagicClass
    Args:
        radius: defaults to 0
    """
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            self.__radius = None
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference"""
        return 2 * math.pi * self.__radius
