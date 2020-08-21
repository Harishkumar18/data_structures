"""
Set Matrix Zeroes
Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = [False for _ in range(rows)]
        col_flag = [False for _ in range(cols)]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    row_flag[row] = True
                    col_flag[col] = True
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row_flag[row] == True or col_flag[col] == True:
                    matrix[row][col] = 0
        return matrix
