"""
Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

Example 1:

Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3
"""


def bisect_left(a, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(a, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def count(arr, target):
    n = len(arr)
    left = bisect_left(arr, target, 0, n)
    right = bisect_right(arr, target, left, n)  # use left as a lower bound
    return right - left


arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
target = 23
print(count(arr, target))
