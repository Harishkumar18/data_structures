"""
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
array) with the smallest (non-negative) difference. Return the difference.
EXAMPLE
Input: {l, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output: 3. That is, the pair (11, 8).

Brute Force
pg 181
The simple brute force way is to just iterate through all pairs, compute the difference, and compare it to the
current minimum difference.
1 int findSmallestDifference(int[] arrayl, int[] array2) {
2 if (arrayl.length == 0 I I array2.length == 0) return -1;
3
4 int min = Integer.MAX_VALUE;
5 for (inti= 0; i < arrayl.length; i++) {
6 for (int j = 0; j < array2.length; j++) {
7 if (Math.abs(arrayl[i] - array2[j]) < min) {
8 min = Math.abs(arrayl[i] - array2[j]);
9 }
10 }
11 }
12 return min;
13 }

the algorithm will take O(AB) time.

Optimal solution:
TC: This algorithm takes O(A log A + B log B) time to sort and O(A + B) time to find the minimum
difference. Therefore, the overall runtime is O(A log A + B log B).
"""

import sys


def find_shortest_difference(arr1, arr2):
    if not len(arr1) or not len(arr2):
        return -1
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    min_diff = sys.maxsize
    while i < len(arr1) and j < len(arr2):
        print(arr1[i], arr2[j])
        if abs(arr1[i] - arr2[j]) < min_diff:
            min_diff = abs(arr1[i] - arr2[j])

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min_diff


arr1 = [1, 2, 11, 15]
arr2 = [4, 12, 19, 23, 127, 235]
print(find_shortest_difference(arr1, arr2))
