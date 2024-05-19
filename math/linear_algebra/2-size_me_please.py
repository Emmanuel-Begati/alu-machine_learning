#!/usr/bin/env python3
def matrix_shape(matrix):
        """
    Calculates the shape of a given matrix.

    Args:
        matrix (list): A nested list representing a matrix. All sublists in the
                       same dimension are assumed to be of the same size/shape.

    Returns:
        list: A list of integers representing the shape of the matrix. Each
              integer corresponds to the size of the matrix in that dimension.
    """

    shape = []
    current_dim = matrix

    while isinstance(current_dim, list):
        shape.append(len(current_dim))
        current_dim = current_dim[0] if current_dim else None

    return shape
