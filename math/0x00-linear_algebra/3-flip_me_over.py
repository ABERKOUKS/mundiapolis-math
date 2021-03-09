import numpy 
def matrix_transpose(matrix):
    matrix=numpy.array(matrix)
    transp=matrix.transpose()
    return transp.tolist()
