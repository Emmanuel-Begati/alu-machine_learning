#!/usr/bin/env python3
def matrix_transpose(matrix):
    # Create an empty result matrix with swapped dimensions
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = [[0] * num_rows for _ in range(num_cols)]

    # Fill in the result matrix with transposed elements
    for i in range(num_rows):
        for j in range(num_cols):
            result[j][i] = matrix[i][j]

    return result
