#!/usr/bin/env python3
def matrix_transpose(matrix):
transpose = []
    for row in range(len(matrix[0])):
        transpose.append([matrix[col][row] for col in range(len(matrix))])
    return transpose
