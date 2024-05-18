#!/usr/bin/env python3
def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Args:
        matrix (list[list]): A 2D matrix (nested list).

    Returns:
        list[int]: A list of integers representing the shape of the matrix.
    """
    shape = []
    current_dim = matrix

    while isinstance(current_dim, list):
        shape.append(len(current_dim))
        current_dim = current_dim[0] if current_dim else None

    return shape
