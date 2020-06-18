"""
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. can you do this in place?
"""


def rotate_matrix(m):
    n = len(m)
    if n<=1:
        return m
    m.reverse()
    for i in range(n):
        for j in range(i):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m


print(rotate_matrix([[1,2],[3,4]]))

print(rotate_matrix([[1]]))

print(rotate_matrix([[1,2, 3],[4, 5, 6], [7,8,9]]))