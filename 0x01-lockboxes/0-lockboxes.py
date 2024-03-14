#!/usr/bin/python3
"""
Module holds a function to determine the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    Attributes:
        boxes: list of lists
    """
    flag = False

    unlocked = [0]
    for box_id, box in enumerate(boxes):
        for key in box:
            if key < len(boxes) and key != box_id and key not in unlocked:
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        flag = True

    return flag
