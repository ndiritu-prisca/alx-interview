#!/usr/bin/python3

def canUnlockAll(boxes):
    boxesLen = len(boxes)
    visited = [False] * boxesLen
    stack = [0]  # Start with the first box unlocked

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if key < boxesLen and not visited[key]:
                stack.append(key)

    return all(visited)
