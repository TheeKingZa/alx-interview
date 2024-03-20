#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations required to
    obtain a file of 'n' characters,
    starting with a file of 1 character and using
    the operation of copying and pasting.

    Args:
    n (int): The desired number of characters in the file.

    Returns:
    int: The minimum number of operations required.
    """
    chars_in_file = 1
    # Initialize the number of characters in the file
    no_of_times_copied = 0
    # Initialize the number of times the file is copied
    counter = 0
    # Initialize the counter for the number of operations

    # Loop until the number of characters in the file reaches 'n'
    while chars_in_file < n:
        remainder = n - chars_in_file
        # Calculate the remaining characters needed

        # Check if the remaining characters can
        # be evenly divided by the current number
        # of characters in the file
        if (remainder % chars_in_file == 0):
            no_of_times_copied = chars_in_file
            # Update the number of times the file is copied
            chars_in_file += no_of_times_copied
            # Update the number of characters in the file
            counter += 2
            # Increment the counter by 2 for the copy and paste operations
        else:
            chars_in_file += no_of_times_copied
            # Update the number of characters in the file
            counter += 1
            # Increment the counter by 1 for the paste operation

    return counter
    # Return the total number of operations required
