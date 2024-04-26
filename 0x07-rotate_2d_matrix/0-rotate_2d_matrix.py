#!/usr/bin/python3
#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    
    Args:
    - matrix (list of lists): The 2D matrix to rotate
    
    Returns:
    - None
    """
    n = len(matrix)  # Get the size of the matrix
    # Traverse the upper triangle of the matrix
    for i in range(n):
        # Start from the diagonal and traverse to the end
        for j in range(i, n):
            # Swap the elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_matrix(matrix):
    # Reverse each row of the matrix
    for row in matrix:
        row.reverse()

def rotate_2d_matrix(matrix):
    n = len(matrix)  # Get the size of the matrix

    # Transpose the matrix
    transpose_matrix(matrix, n)

    # Reverse the transposed matrix
    reverse_matrix(matrix)

    return matrix

def transpose_matrix(matrix, n):
    # Transpose the matrix by swapping elements across the diagonal
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
