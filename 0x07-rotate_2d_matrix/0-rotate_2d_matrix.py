#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    
    Args:
    - matrix (list of lists): The 2D matrix to rotate
    
    Returns:
    - None
    """
    n = len(matrix)  # Get the size of the matrix

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for row in matrix:
        row.reverse()