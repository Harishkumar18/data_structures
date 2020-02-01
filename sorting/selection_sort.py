"""
Description: This algorithm segments the list into two parts: sorted and unsorted. We continuously remove the
smallest element of the unsorted segment of the list and append it to the sorted segment. consider leftmost part of
the list as the sorted segment. We then search the entire list for the smallest element, and swap it with the first
element.After this we know that the first element of the list is sorted, we get the smallest element of the remaining
items and swap it with the second element. This reiterates until the last item of the list is the remaining element
to be examined.

In place algorithm

"""


def selection_sort_algo(nums):
    for i in range(len(nums)):
        lowest_num_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_num_index]:
                lowest_num_index = j
        nums[i], nums[lowest_num_index] = nums[lowest_num_index], nums[i]


# main function
num_list = [12, 12, 8, 3, 20, 11]
selection_sort_algo(num_list)
print(num_list)
