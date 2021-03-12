#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    if len(mat1[0])==len(mat2[0]) and axis==0:
        conc=vstack((mat1, mat2),axis=0) 
        return conc    
    elif len(mat1)==len(mat2) and axis==1:
        conc=hstack(mat1, mat2),axis=1) 
        return conc   
    else:
        return "None"
