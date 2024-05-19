#!/usr/bin/env python3
def matrix_shape(matrix):
    """
    Calculates the transpose of a given 2D matrix.

    Args:
        matrix (list[list]): A 2D matrix (nested list).

    Returns:
        list[list]: The transposed matrix.
    """
    shape = []
    current_dim = matrix

    while isinstance(current_dim, list):
        shape.append(len(current_dim))
        current_dim = current_dim[0] if current_dim else None

    return shape
