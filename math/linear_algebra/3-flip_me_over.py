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

# Example usage
mat1 = [[1, 2], [3, 4]]
print("Original matrix:")
print(mat1)
print("Transposed matrix:")
print(matrix_transpose(mat1))

mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print("Original matrix:")
print(mat2)
print("Transposed matrix:")
print(matrix_transpose(mat2))
