#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
    - True if all boxes can be opened, else False.
    """
    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    visited.add(0)  # Start with the first box

    # Initialize a stack to keep track of keys to explore
    keys_to_explore = boxes[0]

    # Explore keys to open boxes
    while keys_to_explore:
        key = keys_to_explore.pop()  # Get the last key
        if key < 0 or key >= num_boxes or key in visited:
            continue  # Skip invalid keys or keys to already visited boxes
        visited.add(key)  # Mark the box as visited
        keys_to_explore.extend(boxes[key])  # Add keys from the current box to explore

    # Check if all boxes have been visited
    return len(visited) == num_boxes

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False
