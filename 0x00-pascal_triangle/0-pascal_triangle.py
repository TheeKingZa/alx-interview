#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle up to the nth row.

    Raises:
        ValueError: If n is less than or equal to 0.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        raise ValueError("n must be greater than 0")
    
    # Initialize Pascal's triangle with the first row [1]
    pascal = [[1]]
    
    # Iterate over each row from the second row up to the nth row
    for i in range(1, n):
        # Create a new row and initialize it with 1 (the first element)
        row = [1]
        # Get the previous row
        prev = pascal[i - 1]
        
        # Iterate over each element of the previous row (except the last one)
        for j in range(len(prev) - 1):
            # Calculate the new element by summing up the current and next element
            new = prev[j] + prev[j + 1]
            # Append the new element to the current row
            row.append(new)
        
        # Append 1 to the end of the current row (the last element)
        row.append(1)
        
        # Append the current row to Pascal's triangle
        pascal.append(row)
    
    # Return Pascal's triangle
    return pascal
