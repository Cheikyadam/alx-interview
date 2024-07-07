#!/usr/bin/python3
"""LockBoxes Python"""


def canUnlockAll(boxes):
    """main function"""
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    for i in range(1, len(boxes)):
        if (isUnlock(i, boxes)) is False:
            return False
    return True


def isUnlock(box_index, boxes):
    """To check if a box is unlocked or not"""
    for i in range(0, len(boxes)):
        if (i != box_index):
            box = boxes[i]
            if box_index in box:
                return True
    return False
