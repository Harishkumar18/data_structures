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


def setZeroes(self, matrix):
    m = len(matrix)
    if m == 0:
        return
    n = len(matrix[0])

    row_zero = False
    for i in range(m):
        if matrix[i][0] == 0:
            row_zero = True
    col_zero = False
    for j in range(n):
        if matrix[0][j] == 0:
            col_zero = True

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    if col_zero:
        for j in range(n):
            matrix[0][j] = 0
    if row_zero:
        for i in range(m):
            matrix[i][0] = 0