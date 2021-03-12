#!/usr/bin/env python3
def matrix_transpose(matrix):
    transpose = []
    for m in range(len(matrix[0])):
        transpose.append([matrix[n][m] for n in range(len(matrix))])
    return transpose
