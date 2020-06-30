"""
Quick Sort I Runtime: O(n log( n)) average, O(n2 ) worst case. Memory: 0( log(n)).
In quick sort we pick a random element and partition the array, such that all numbers that are less than the
partitioning element come before all elements that are greater than it. The partitioning can be performed
efficiently through a series of swaps (see below).
If we repeatedly partition the array (and its sub-arrays) around an element, the array will eventually become
sorted. However, as the partitioned element is not guaranteed to be the median (or anywhere near the
median), our sorting could be very slow. This is the reason for the 0( n2) worst case runtime.
"""


def QuickSort(inp_arr, left, right):
    partition_index = partition(inp_arr, left, right)
    if left<partition_index:
        QuickSort(inp_arr, left, partition_index-1)
    if partition_index<right:
        QuickSort(inp_arr, partition_index, right)


def partition(inp_arr, left, right):
    pivot = inp_arr[(right+left)//2]
    while left < right:
        while inp_arr[left] < pivot:
            left += 1
        while inp_arr[right] > pivot:
            right -= 1
        if left <= right:
            inp_arr[left], inp_arr[right] = inp_arr[right], inp_arr[left]
            left += 1
            right -= 1
    return left


# inp_arr = [12, 11, 13, 7, 6, 5]
inp_arr = [4, 8, 2, 0, 5, 3]
QuickSort(inp_arr, 0, len(inp_arr)-1)
print(inp_arr)
