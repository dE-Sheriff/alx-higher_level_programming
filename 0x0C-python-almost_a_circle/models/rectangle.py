#!/usr/bin/python3

"""
A class Rectangle that inherits from Base
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangular class inheriting Base
    """
    # __width = 0
    # __height = 0
    # __x = 0
    # __y = 0
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intializing Rectangle class with following parameters
        :param width: Width of the Rectangle
        :param height: Height of the Rectangle
        :param x: What is x
        :param y: What is y
        :param id: id of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        
    @property
    def width(self):
        """Obtain the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """Obtain the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """sets the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """Obtain the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Obtain the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y of the Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
