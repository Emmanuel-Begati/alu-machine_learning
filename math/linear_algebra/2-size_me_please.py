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

# Example usage
mat1 = [[1, 2], [3, 4]]
print("Shape of mat1:", matrix_shape(mat1))

mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print("Shape of mat2:", matrix_shape(mat2))
