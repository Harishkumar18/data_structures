"""Write a program to cyclically rotate an array by one."""


def rotate_arr_by_one(arr):
    return [arr[-1]]+arr[:-1]


arr = [1,2,3,4,5]
res = rotate_arr_by_one(arr)
print(res)