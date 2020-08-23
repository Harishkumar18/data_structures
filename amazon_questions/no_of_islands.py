"""Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

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
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        no_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # process only when element is 1 otherwise leave it
                if grid[i][j] == "1":
                    no_of_islands += self.dfs(grid, i, j)
        return no_of_islands

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
        # need to mark the current value as 0 so that we won't process it again
        grid[i][j] = "0"
        # mark all the connected nodes also as 0
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        return 1
