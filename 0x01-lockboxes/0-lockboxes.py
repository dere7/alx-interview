#!/usr/bin/python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """
    checks if it is possible to open all boxes from open first box
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True

    >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
    True

    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    """
    opened = set()
    opened.add(0)
    for i in range(len(boxes)):
        for j in opened.copy():
            opened.update(boxes[j])

    return set(range(len(boxes))).issubset(opened)
