#!/usr/bin/python3
""" Module: This is the matrix division module"""


err = 'matrix must be a matrix (list of lists) of integers/floats'


def matrix_divided(matrix, div):
    """A simple function that divides all elements of a matrix"""
    if not type(matrix) in [list]:
        raise TypeError(err)

    size = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)
        if size == 0:
            size = row.__len__()
        elif size != row.__len__():
            raise TypeError('Each row of the matrix must have the same size')
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(err)
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(i / div, 2) for i in rows] for rows in matrix]
