"""
Find the "Kth" max and min element of an array
"""
import heapq


def kth_max_min(arr, k):
    arr.sort()
    return arr[k-1], arr[-k]


def kth_smallest(arr, k):
    smallest = []
    for i in arr:
        if len(smallest) < k:
            heapq.heappush(smallest, -i)
        else:
            heapq.heappushpop(smallest, -i)
    return -smallest[0]


k = 3
minimum = kth_smallest([20,2,5,10,8], k)
print("minimum", minimum)