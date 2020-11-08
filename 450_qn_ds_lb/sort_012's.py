"""
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
"""


def sort_012(arr):
    low = mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid+=1
            low+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            mid+=1
            high-=1
    return arr


result = sort_012([2,1,2,0,1,0])
print(result)