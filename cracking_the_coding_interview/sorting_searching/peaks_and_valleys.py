"""
Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
array of integers, sort the array into an alternating sequence of peaks and valleys.

This algorithm takes O ( n) time.
"""


def peak_valley_order(arr):
    for i in range(1, len(arr), 2):
        biggestIndex = find_biggest_index(arr, i-1, i, i+1)
        if i!=biggestIndex:
            arr[i], arr[biggestIndex] = arr[biggestIndex], arr[i]
    return arr


def find_biggest_index(arr, a, b,c):
    arr_len = len(arr)
    avalue = arr[a] if 0 <= a < arr_len else -1
    bvalue = arr[b] if 0 <= b < arr_len else -1
    cvalue = arr[c] if 0 <= c < arr_len else -1
    max_elem = max(avalue, bvalue, cvalue)
    if max_elem == avalue:
        return a
    elif max_elem==bvalue:
        return b
    else:
        return c


arr = [9, 1, 0, 4, 8, 7]
print(peak_valley_order(arr))