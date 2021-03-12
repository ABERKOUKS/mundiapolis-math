#!/usr/bin/env python3
def matrix_shape(matrix):
  if type(matrix[0]) is list:
    return [len(matrix)]+matrix_shape(matrixe[0])
  else:
    return [len(matrix)]
  return matrix.shape
