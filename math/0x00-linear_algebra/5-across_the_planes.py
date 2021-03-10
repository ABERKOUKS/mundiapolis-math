import numpy 
def add_matrices2D(mat1, mat2):
    mat1=numpy.asarray(mat1)
    mat2=numpy.asarray(mat2)
    if mat1.shape == mat2.shape:
        addM=numpy.add(mat1, mat2) 
        return addM.tolist()
    else:
        return "None"
