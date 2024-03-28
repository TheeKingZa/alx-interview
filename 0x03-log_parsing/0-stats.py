#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
    Method to print aggregated status codes and total file size
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    # Print total file size
    print("File size: {}".format(total_file_size))
    
    # Print status codes with their counts, excluding those with count 0
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


# Initialize variables
total_file_size = 0
code = 0
counter = 0

# Initialize dictionary to store status codes and their counts
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0
}

try:
    # Iterate over each line from standard input
    for line in sys.stdin:
        # Split the line by whitespace
        parsed_line = line.split()  # ✄ trimming
        
        # Reverse the parsed line
        parsed_line = parsed_line[::-1]  # inverting

        # Check if the parsed line has more than 2 elements
        if len(parsed_line) > 2:
            # Increment counter
            counter += 1

            # Check if the counter is less than or equal to 10
            if counter <= 10:
                # Add the file size to total_file_size
                total_file_size += int(parsed_line[0])  # file size
                
                # Get the status code
                code = parsed_line[1]  # status code

                # Check if the status code is in the dictionary
                if (code in dict_sc.keys()):
                    # Increment the count for the status code
                    dict_sc[code] += 1

            # Check if the counter is equal to 10
            if (counter == 10):
                # Print aggregated status codes and total file size
                print_msg(dict_sc, total_file_size)
                
                # Reset counter
                counter = 0

finally:
    # Print aggregated status codes and total file size
    print_msg(dict_sc, total_file_size)
