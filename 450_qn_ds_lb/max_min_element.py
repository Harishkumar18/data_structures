"""
Find the maximum and minimum element in an array
"""


def find_max_min(arr):
    min = 2**32
    max = -2**32
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return (min, max)



print(find_max_min([2,3,4,1,5]))