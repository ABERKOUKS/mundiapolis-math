#!/usr/bin/env python3
import numpy 
def cat_matrices2D(mat1, mat2, axis=0):
    if len(mat1[0])==len(mat2[0]) and axis==0:
        conc=numpy.concatenate((mat1, mat2),axis=0) 
        return conc.tolist()       
    elif len(mat1)==len(mat2) and axis==1:
        conc=numpy.concatenate((mat1, mat2),axis=1) 
        return conc.tolist()     
    else:
        return "None"
