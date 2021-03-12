#!/usr/bin/env python3
def matrix_shape(matrix):
  if type(matrix[0]) is not list:
    return int([len(matrix)])
  else:
    return int([len(matrix)]+matrix_shape(matrixe[0]))
