"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear
path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
(i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different, and they share an edge or
a corner). The length of a clear path is the number of visited cells of this path.


Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # total_rows -> this is the total length of the given grid
        total_rows = len(grid)

        # if top-left (i.e (0,0)) or bottom-right (i.e (total_rows-1),(total_rows-1)) is not zero,
        # we cant find start and end tail position of given grid -> so return -1
        if grid[0][0] or grid[total_rows - 1][total_rows - 1] != 0: return -1

        # shortest_path -> starting point of the path is (0,0) and start distance is 1
        shortest_path = [(0, 0, 1)]

        # assign -> starting point of the path as 1
        grid[0][0] = 1

        # Iterate through for the shortest path with start row, start column with assigned distance.
        for row, column, distance in shortest_path:

            # if we reached the ending or tail point then return distance in shortest path
            if row == total_rows - 1 and column == total_rows - 1: return distance

            # We have to check the shortest path in all 8 directions
            directions = [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1), (row, column - 1),
                          (row, column + 1), (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]

            # Check the path using row and column in directions
            for point_x, point_y in directions:
                # check points lie within the grid and the particular direction is zero -> then change direction to 1
                if 0 <= point_x < total_rows and 0 <= point_y < total_rows and grid[point_x][point_y] == 0:
                    grid[point_x][point_y] = 1

                    # append the path to shortest path
                    shortest_path.append((point_x, point_y, distance + 1))

        # -1 -> if there is no path.
        return -1


solution = Solution()
assert 4 == solution.shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]])
assert -1 == solution.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]])
assert -1 == solution.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]])
assert 5 == solution.shortestPathBinaryMatrix(grid=[[0, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 1, 0]])
assert 2 == solution.shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]])
