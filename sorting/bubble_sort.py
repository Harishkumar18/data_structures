"""
Description : comparing the elements in pairs (first two elements  and so on) until the large elements bubble up to the
end of the list

In place algorithm
stable algorithm
"""


def bubble_sort_algo(nums):
    # we are setting the swapped function tom run the loop atleast once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


# main function
num_list = [5, 2, 1, 8, 4]
bubble_sort_algo(num_list)
print(num_list)
