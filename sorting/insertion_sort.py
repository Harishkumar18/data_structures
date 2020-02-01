"""Description : An array is partitioned into a "sorted" subarray and an "unsorted" subarray. At the beginning,
the sorted subarray contains only the first element of our original array. The first element in the unsorted array is
evaluated so that we can insert it into its proper place in the sorted subarray.The insertion is done by moving all
elements larger than the new element one position to the right. Continue doing this until our entire array is sorted.

In-place algorithm
stable algorithm
"""


def insertion_sort_algo(nums):
    for i in range(1, len(nums)):
        currentindex = i
        currentvalue = nums[i]
        while currentindex>0 and nums[currentindex-1] > nums[currentindex]:
            nums[currentindex] = nums[currentindex-1]
            nums[currentindex-1] = currentvalue
            currentindex = currentindex-1


# main function
num_list = [9, 1, 15, 28, 6, 3]
insertion_sort_algo(num_list)
print(num_list)
