"""
binary search
"""


def binary_search(inp_arr, target):
    left = 0
    right = len(inp_arr)
    return bt(inp_arr, left, right, target)


def bt(inp_arr, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if inp_arr[mid] < target:
            left = mid + 1
        elif inp_arr[mid] > target:
            right = mid
        else:
            return mid
    return -1


def recursive_bt(inp_arr, left, right, target):
    if left>=right:
        return -1
    mid = (right+left)//2
    if inp_arr[mid]<target:
        return recursive_bt(inp_arr, mid+1, right, target)
    elif inp_arr[mid]>target:
        return recursive_bt(inp_arr, left, mid, target)
    else:
        return mid




a = [1, 4, 5, 6, 8]
# print(binary_search(a, 8))
print(recursive_bt(a, 0, len(a), 8))