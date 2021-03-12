import numpy 
def cat_arrays(arr1, arr2):
    conc=numpy.concatenate((arr1, arr2)) 
    return conc.tolist()

