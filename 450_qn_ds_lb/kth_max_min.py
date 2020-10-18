"""
Find the "Kth" max and min element of an array
"""


def kth_max_min(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]


k = 3
min, max = kth_max_min([20,2,5,10,8], k)
print(min)
print(max)