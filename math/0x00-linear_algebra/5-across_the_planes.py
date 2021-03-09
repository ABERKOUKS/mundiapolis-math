import numpy 
def add_matrices2D(mat1, mat2):
    mat1=numpy.array(mat1)
    mat2=numpy.array(mat2)
    if mat1.shape == mat2.shape:
        addM=np.add(mat1, mat2) 
        return addM
    else:
        return "None"
