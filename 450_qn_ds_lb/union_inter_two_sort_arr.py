"""
Find the Union and Intersection of the two sorted arrays.
"""


def find_union(arr1, arr2):
    res = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        else:
            res.append(arr2[j])
            j += 1
    if j != len(arr2):
        while j < len(arr2):
            res.append(arr2[j])
            j += 1
    return res


def find_intersection(arr1, arr2):
    res = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return res


arr1 = [1, 2, 4, 5, 9]
arr2 = [2, 6, 8, 9, 10, 11]
print(find_union(arr1, arr2))
