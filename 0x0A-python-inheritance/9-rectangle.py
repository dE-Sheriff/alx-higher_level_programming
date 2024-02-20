#!/usr/bin/python3
"""
module: 8-rectangle:
with class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initialises the attributes: width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """define a area method in the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """__str__ method for return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
