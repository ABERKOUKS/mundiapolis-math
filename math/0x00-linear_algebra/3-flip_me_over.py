#!/usr/bin/env python3
import numpy 
def matrix_transpose(matrix):
    matrix=numpy.array(matrix)
    transp=matrix.transpose()
    return transp.tolist()
