import numpy 
def add_arrays(mat1, mat2):
    mat1=numpy.array(mat1)
    mat2=numpy.array(mat2)
    if mat1.shape == mat2.shape:
        add=np.add(mat1, mat2) 
        return add
    else:
        return "None"
