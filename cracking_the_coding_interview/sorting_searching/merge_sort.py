"""
implementation of merge sort algo
TC: O(n log n)
SC:o(n)
Stable algorithm
type - Not inplace algo
it won't modify the existing array but it will create a new array
TODO: Need to fix giving wrong output
"""


def merge(inp_arr, lb, mid, ub):
    n1 = mid - lb + 1
    n2 = ub - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = inp_arr[i]
    for j in range(0, n2):
        R[j] = inp_arr[mid + 1 + j]
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            inp_arr[k] = L[i]
            i += 1
        else:
            inp_arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        inp_arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        print("n2", n2)
        print("j", j)
        inp_arr[k] = R[j]
        j += 1
        k += 1


def MergeSort(inp_arr, lb, ub):
    if lb < ub:
        mid = (lb + (ub - lb // 2))
        MergeSort(inp_arr, lb, mid)
        MergeSort(inp_arr, mid + 1, ub)
        merge(inp_arr, lb, mid, ub)


# inp_arr = [10, 6, 2, 15, 0]
inp_arr = [12, 11, 13, 7, 6, 5]
MergeSort(inp_arr, 0, len(inp_arr)-1)
print(inp_arr)
