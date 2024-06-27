#!/usr/bin/python3
"""pascal_triangle algo with python"""


def pascal_triangle(n):
    if n > 0:
        triangle = init_triangle(n)
        if n <= 2:
            return triangle
        else:
            for i in range(2, n):
                for j in range(1, i):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
            return triangle


def init_triangle(n):
    triangle = []
    for j in range(n):
        row = []
        for i in range(j+1):
            if i == 0 or i == j:
                row.append(1)
            else:
                row.append(0)
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
