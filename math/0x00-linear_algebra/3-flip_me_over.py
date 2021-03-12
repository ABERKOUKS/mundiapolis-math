#!/usr/bin/env python3
def matrix_transpose(matrix):
    trans=[]
    trans =[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans
