"""
Vmware interview question2: sort the positve ansd negative integers in
o(1) space.
"""


def sort_array(arr):
    i, j = 0,1
    while j<len(arr):
        if arr[i]<0:
            i+=1
            j+=1
        else:
            if arr[j]<=0:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
            j+=1



a = [-5, 0, 1, -5, -2]
sort_array(a)
print(a)