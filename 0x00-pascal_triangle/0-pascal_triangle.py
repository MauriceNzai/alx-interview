#!/usr/bin/python3
"""
printing pascal triangle

In this triangle, each number is equal to sum of two number directly above it.
"""


def pascal_triangle(n):
    """
    returns tringle of size n

    args:
        n: the number of rows to print
    """

    # base case: return empty list if n <= 0
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
