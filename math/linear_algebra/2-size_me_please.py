#!/usr/bin/env python3
import numpy as np

def matrix_shape(matrix):
    # Convert the input matrix to a NumPy array
    np_matrix = np.array(matrix)

    # Get the shape of the array
    shape = np_matrix.shape

    # Convert the shape tuple to a list of integers
    shape_list = list(shape)

    return shape_list

# Example usage
mat1 = [[1, 2], [3, 4]]
print("Shape of mat1:", matrix_shape(mat1))

mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print("Shape of mat2:", matrix_shape(mat2))
