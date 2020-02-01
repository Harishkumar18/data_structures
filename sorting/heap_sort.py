"""Description: Heap Sort works by "removing" elements from the heap part of the array one-by-one and adding them to
the sorted part of the array. Before we get further into the explanation and revisit the heap data structure,
we should mention a few attributes of Heap Sort itself. Heap Sort is another example of an efficient sorting
algorithm. Its main advantage is that it has a great worst-case runtime of O(n*logn) regardless of the input data. As
the name suggests, Heap Sort relies heavily on the heap data structure - a common implementation of a Priority Queue.

In Place algorithm

Heap Sort is the sorting algorithm of choice in the Linux Kernel

Sorting time of Heap Sort is O(n*logn) both on average and worst-case. While qsort is about 20% faster on average, it
suffers from an exploitable O(n*n) worst-case behavior and extra memory requirements that make it less suitable for kernel use.
"""
from heapq import heappush, heappop


def heap_sort_algo(nums):
    heapify_list, ordered = list(), list()
    for item in nums:
        heappush(heapify_list, item)
    while heapify_list:
        ordered.append(heappop(heapify_list))
    return ordered


# main function
num_list = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
sorted_list = heap_sort_algo(num_list)
print(sorted_list)