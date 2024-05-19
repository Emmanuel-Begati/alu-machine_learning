#!/usr/bin/env python3
"""
This is a file that adds two matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices element-wise.

    Args:
        mat1 (list of list of int/float): First input 2D matrix.
        mat2 (list of list of int/float): Second input 2D matrix.

    Returns:
        list of list of int/float or None: New matrix containing the element-wise
        sum of mat1 and mat2. If mat1 and mat2
        are not the same shape, returns None.
    """
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) 
                                     for row1, row2 in zip(mat1, mat2)):
        return None

    return [[a + b for a,b in zip(row1,row2)] for row1,row2 in zip(mat1, mat2)]
