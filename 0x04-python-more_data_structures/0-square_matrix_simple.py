#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        new_row = []
        for col in rows:
            new_row.append(col * col)
        new_matrix.append(new_row)
    return new_matrix
