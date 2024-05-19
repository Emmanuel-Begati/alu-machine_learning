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
    
    Example:
        >>> matrix_shape([[1, 2], [3, 4]])
        [2, 2]
        
        >>> matrix_shape([
                [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
                [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
            ])
        [2, 3, 5]
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape