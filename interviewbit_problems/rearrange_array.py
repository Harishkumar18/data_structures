"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
"""


def rearrange(A):
    if not A:
        return []
    n = len(A)
    for i in range(0, n):
        A[i] += (A[A[i]] % n) * n
    for i in range(0, n):
        A[i] = int(A[i] / n)
    return A


print(rearrange([4, 0, 2, 1, 3]))
