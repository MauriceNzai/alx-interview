#!/usr/bin/python3
"""
Minimum operations funtion

In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    determines minimum number of operations to result exactly n H characters
    """
    cache = {}

    def helper(screen, clipboard):
        """
        Helper function within the main function for efficieny
        """
        if (screen, clipboard) in cache:
            return cache[(screen, clipboard)]
        if screen == n:
            return 0
        if screen > n:
            return float('inf')

        copy_paste = helper(screen + screen, screen) + 2
        paste = float('inf')

        if clipboard:
            paste = helper(screen + clipboard, clipboard) + 1

        cache[(screen, clipboard)] = min(copy_paste, paste)

        return cache[(screen, clipboard)]

    return helper(1, 0)
