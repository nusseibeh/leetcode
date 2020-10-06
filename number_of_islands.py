#!/bin/bash python3

"""
Problem Definition
-------------------

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

from collections import deque

def check(grid, x, y, visited):
    return (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])) and (int(grid[x][y]) == 1 and not visited[x][y])


def search(grid, visited, i, j):
    row = [1, 0, 0, -1]
    col = [0, -1, 1, 0]

    q = deque()
    q.append((i,j))

    visited[i][j] = True

    while q:
        x,y = q.popleft()

        for k in range(4):
            if check(grid, x + row[k], y + col[k], visited):
                visited[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))


def numberOfIslands(grid):
    (m,n) = (len(grid),len(grid[0]))
    
    visited = [[ False for x in range(n)] for y in range(m)]

    islands = 0

    for i in range(m):
        for j in range(n):
            if int(grid[i][j]) == 1 and not visited[i][j]:
                search(grid, visited, i, j)
                islands += 1
    
    return islands


if __name__ == '__main__':
    # Driver function
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
           ]

    # Function call
    print("There are {} islands".format(numberOfIslands(grid)))