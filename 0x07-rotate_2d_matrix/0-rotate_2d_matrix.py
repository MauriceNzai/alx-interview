#!/usr/bin/python3
"""
rotating 2D matrix
"""
def transpose(matrix):
    """
    trnsposes the matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix

def reverse_rows(row, start, end):
    """
    reverse each row of the transposed matrix
    """
    while start < end:
        temp=row[start]
        row[start]=row[end]
        row[end]=temp
        start=start+1
        end=end-1

def rotate_2d_matrix(matrix):
    """
    rotates 2D matrix
    """
    if not matrix:
        return
    if len(matrix) == 1:
        return

    transpose(matrix)

    for i in range(len(matrix[0])):
        reverse_rows(matrix[i], 0, len(matrix[i])-1)
