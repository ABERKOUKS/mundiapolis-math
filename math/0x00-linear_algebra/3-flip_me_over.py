#!/usr/bin/env python3
def matrix_transpose(matrix):
    trans = []
    for m in range(len(matrix[0])):
        trans.append([matrix[n][m]] for n in range(len(matrix)))
    return trans
