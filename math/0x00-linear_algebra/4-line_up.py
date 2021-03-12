#!/usr/bin/env python3 
def add_arrays(mat1, mat2):
    if len(mat1) == len(mat2):
        add=[[(mat1[i]+mat2[i]) for i in range(len(mat1))]]
        return add
    else:
        return "None"  
