#!/usr/bin/python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """function here"""
    n = len(matrix)
    new_matrix = []
    for i in range(n):
        row = []
        k = 0
        for j in range(n-1, -1, -1):
            row.append(matrix[j][i])
            k = k + 1
        new_matrix.append(row)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]
