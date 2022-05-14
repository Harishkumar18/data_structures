"""
Python interview question

Sort 0's and 1's left to right
0's on the left and 1's on the right

- Time complexity O(n)
- Space complexity O(1) - It should be in place, cannot create a new array
- Cannot use the length function
"""

lst = [0, 1, 1, 1, 0, 0, 1, 0, 1]


def sort_01_with_len(lst):
    left, right = 0, len(lst)-1
    while left < right:

        if lst[left] == 0:
            left += 1
        if lst[left] == 1:
            lst[left], lst[right] = lst[right], lst[left]
            right -= 1

def sort_01(lst):
    left = 0
    right = 1
    try:
        while left or right:
            if lst[left] == 0:
                left += 1
                right +=1
            if lst[left] == 1 and lst[right] == 1:
                right += 1
            if lst[left] == 1 and lst[right] == 0:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
    except IndexError:
        pass


sort_01(lst)
print(lst)
