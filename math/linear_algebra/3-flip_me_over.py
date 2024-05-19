#!/usr/bin/env python3
"""
This module provides a function to transpose a matrix.

The `matrix_transpose` function takes a 2D matrix (a list of lists) and returns
a new matrix that is the transpose of the input matrix.
"""


def matrix_transpose(matrix):
    """
    Transposes the given 2D matrix.

    Args:
        matrix (list of list of int/float): A 2D list where each sublist
                                            represents a row of the matrix.
    Returns:
        list of list of int/float: A new 2D list where each sublist represents
        a row of the transposed matrix (i.e., the columns
        of the original matrix become the rows of the new matrix).
    Example
        >>> matrix_transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
        >>> matrix_transpose([[1, 2], [3, 4], [5, 6]])
        [[1, 3, 5], [2, 4, 6]]
    """
    # Create an empty result matrix with swapped dimensions
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = [[0] * num_rows for _ in range(num_cols)]

    # Fill in the result matrix with transposed elements
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][i] = matrix[i][j]

    return result
