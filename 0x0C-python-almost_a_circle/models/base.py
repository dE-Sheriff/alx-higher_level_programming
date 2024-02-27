#!/usr/bin/python3

"""
Base model for all tasks
"""

class Base:
    """
    The Base Model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Initializing the Base class for any object with id
        id: id of the Base oject
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
