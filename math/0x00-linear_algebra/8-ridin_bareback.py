#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    if len(mat1[0])== len(mat2):
        mat1= numpy.asarray(mat1)
        mat2= numpy.asarray(mat2)
        mult=mat1.dot(mat2) 
        return mult.tolist()    
    else:
        return "None"
