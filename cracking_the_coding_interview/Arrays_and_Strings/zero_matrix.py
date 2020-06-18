"""
Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
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


def set_zeros(mat):
    m, n = len(mat), len(mat[0])
    if m < 1:
        return mat
    if n < 1:
        return mat
    rowzeroflag, colzeroflag = False, False
    for j in range(m):
        if mat[0][j] == 0:
            rowzeroflag = True
            break
    for i in range(n):
        if mat[i][0] == 0:
            colzeroflag = True
            break
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
    if rowzeroflag:
        for j in range(n):
            mat[0][j] = 0
    if colzeroflag:
        for i in range(m):
            mat[i][0] = 0
    return mat


print(set_zeros([[1,1,1],[1,0,1],[1,1,1]]))

print(set_zeros([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
