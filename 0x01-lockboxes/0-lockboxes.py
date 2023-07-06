#!/usr/bin/python3
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    num_boxes = len(boxes)  # Total number of boxes
    visited = set()  # Set to track visited boxes
    visited.add(0)  # Mark the first box as visited

    queue = [0]  # Initialize the queue with the first box

    while queue:
        current_box = queue.pop(0)

        # Check the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box and it hasn't been visited before
            if key < num_boxes and key not in visited:
                visited.add(key)
                queue.append(key)

        # If we have visited all the boxes, return True
        if len(visited) == num_boxes:
            return True

    return False
