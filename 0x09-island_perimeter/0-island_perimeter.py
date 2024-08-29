#!/usr/bin/python3
"""My island code here"""


def island_perimeter(grid):
    """Island perimeter"""

    if grid is None or len(grid) == 0:
        return 0

    for row in grid:
        width = len(row)
        break
    height = 0
    for row in grid:
        height += 1
    p = 0
    for i in range(0, height):
        for j in range(0, width):
            if grid[i][j] == 1:
                if (j-1) < 0:
                    p += 1
                else:
                    if grid[i][j-1] == 0:
                        p += 1
                if (j+1) >= width:
                    p += 1
                else:
                    if grid[i][j+1] == 0:
                        p += 1
                if (i-1) < 0:
                    p += 1
                else:
                    if grid[i-1][j] == 0:
                        p += 1
                if (i+1) >= height:
                    p += 1
                else:
                    if grid[i+1][j] == 0:
                        p += 1
    return p
