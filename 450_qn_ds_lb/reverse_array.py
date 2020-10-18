"""
Reverse the array
"""


def reverse_array(arr):
    n = len(arr)-1
    reversed = []
    while n >= 0:
        reversed.append(arr[n])
        n -= 1
    return reversed


arr = [1,2,3,4,5]
print(reverse_array(arr))