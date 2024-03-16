#!/usr/bin/python3
"""Module to determine if a list of boxes contain keys to other boxes"""

def canUnlockAll(boxes):
    """Function to determine if keys from one box can unlock all other boxes"""

    # Iterate over each key (box index) from 1 to len(boxes) - 1
    for key in range(1, len(boxes) - 1):
        visited = False
        # Iterate over each box to check if the key can unlock any box
        for box_index in range(len(boxes)):
            # Check if the key is in the current box and it's not the current box itself
            visited = key in boxes[box_index] and key != box_index
            # If the key can unlock a box, set visited to True and break the loop
            if visited:
                break
        # If the key cannot unlock any box, return False
        if visited is False:
            return visited
    # If all keys can unlock at least one box, return True
    return True
