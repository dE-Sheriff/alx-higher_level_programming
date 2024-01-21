#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        line = []
        for col in row:
            line.append("{:d}".format(col))
        print(" ".join(line))
