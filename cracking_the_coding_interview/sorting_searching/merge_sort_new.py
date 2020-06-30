"""
implementation of merge sort algo
TC: O(n log n)
SC:o(n)
Stable algorithm
type - Not inplace algo
it won't modify the existing array but it will create a new array
"""


def MergeSort(inp_arr):
    if len(inp_arr)>1:
        left = 0
        right= len(inp_arr)
        mid = right//2
        # mid = left+(right-left//2)
        L = inp_arr[:mid]
        R = inp_arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i, j, k = 0, 0, 0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                inp_arr[k] = L[i]
                i+=1
            else:
                inp_arr[j] = R[j]
                j+=1
            k+=1
        while i<len(L):
            inp_arr[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            inp_arr[k] = R[j]
            j+=1
            k+=1



inp_arr = [10, 6, 2, 15, 0]
inp_arr = [12, 11, 13, 7, 6, 5]
MergeSort(inp_arr)
print(inp_arr)