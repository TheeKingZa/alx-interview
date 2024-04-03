#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given data is a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    * A character in UTF-8 can be 1 to 4 bytes long
    * The data set can contain multiple characters
    * Each integer represents 1 byte of data,
    * therefore you only need to handle the 8 least
    * significant bits of each integer
    """

    # Initialize a counter to keep track of
    # the number of continuation bytes expected
    num_continuation_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if the current byte is a continuation byte
        if num_continuation_bytes > 0:
            # If it's a continuation byte, decrement the counter
            num_continuation_bytes -= 1
            # If the current byte is not in the format '10xxxxxx',
            # return False
            if not (0b10000000 <= byte <= 0b10111111):
                return False
        else:
            # If it's not a continuation byte,
            # determine the number of continuation bytes expected
            if byte >= 0b11110000:
                # 4-byte character: start byte '11110xxx'
                num_continuation_bytes = 3
            elif byte >= 0b11100000:
                # 3-byte character: start byte '1110xxxx'
                num_continuation_bytes = 2
            elif byte >= 0b11000000:
                # 2-byte character: start byte '110xxxxx'
                num_continuation_bytes = 1
            # If the current byte is not in the format '0xxxxxxx', return False
            elif byte >= 0b10000000:
                return False

    # If all bytes have been processed and there are
    # no remaining continuation bytes expected, return True
    return num_continuation_bytes == 0
