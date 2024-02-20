#!/usr/bin/python3
"""
Module: 1-my_list
MyList inherits from list"""


class MyList(list):
    """that prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        """prints the sorted elements of the list"""
        print(sorted(list(self)))
