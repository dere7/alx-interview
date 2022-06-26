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

    >>> canUnlockAll([[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]])
    True

    >>> canUnlockAll([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False

    >>> canUnlockAll([[0]])
    True
    """
    opened = set()
    opened.add(0)
    for i in range(len(boxes)):
        for j in opened.copy():
            try:
                opened.update(boxes[j])
            except IndexError:
                pass

    return set(range(len(boxes))).issubset(opened)
