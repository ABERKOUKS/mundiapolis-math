#!/usr/bin/env python3 
def add_arrays(mat1, mat2):
    if len(mat1) == len(mat2):
        return "None"
    else:
        add=[[(mat1[i]+mat2[i]) for j in range(len(mat1))]]
        return add
        
