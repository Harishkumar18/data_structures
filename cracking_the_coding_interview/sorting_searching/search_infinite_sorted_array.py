"""
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt ( i) method that returns the element at index i in
0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.

TC: It turns out that not knowing the length didn't impact the runtime of the search algorithm. We find the
length in O( log n) time and then do the search in 0( log n) time. Ouroverall runtime isO(log n ),just
as it would be in a normal array.
"""


def binary_search(arr, low, high, key):
    # normal algo
    pass


def findPos(arr, key):
    low, high, val = 0, 1, arr[0]

    while val < key:
        low = high
        high = 2 * high
        val = arr[high]

    return binary_search(arr, low, high, key)


arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
res = findPos(arr, 10)
