#!/usr/bin/python3
'''
    You have n number of locked boxes in front of you.
    Numbered sequentially from 0 to n - 1.
    Each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''Method that determines if all boxes can be opened'''
    boxesLen = len(boxes)
    visitedBox = [False] * boxesLen
    stack = [0]

    while stack:
        current_box = stack.pop()
        visitedBox[current_box] = True

        for key in boxes[current_box]:
            if key < boxesLen and not visitedBox[key]:
                stack.append(key)

    return all(visitedBox)
