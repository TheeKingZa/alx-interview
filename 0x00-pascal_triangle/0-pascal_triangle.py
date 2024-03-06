#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []
    # Return an empty list if n is less than or equal to 0

    triangle = []
    # Initialize an empty list to store the triangle
    for i in range(n):
        # Iterate over each row of the triangle
        row = [1] * (i + 1)
        # Initialize each row with 1s
        for j in range(1, i):
            # Iterate over each element of
            # the row (excluding the first and last)
            # Calculate the value of the element
            # using the values from the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        # Append the completed row to the triangle

    return triangle
    # Return the generated Pascal's triangle
