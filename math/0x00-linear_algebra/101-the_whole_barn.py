#!/usr/bin/env python3
def add_matrices(mat1, mat2):
    x1=np.asarray(mat1)
    x2=np.asarray(mat2)
    if x1.shape == x2.shape:
        return np.add(x1, x2).tolist()
    else:
        return "None"
