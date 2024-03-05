#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to row n
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    triangle = []  # Initialize the Pascal's triangle

    # Generate each row of Pascal's triangle
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            # Generate elements between the first and last element of the row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print(" ".join([str(x) for x in row]))
