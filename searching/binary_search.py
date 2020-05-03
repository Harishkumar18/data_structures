# Function call
def binarySearch(arr, left, right, x):
    mid_ele = right-(right-left)//2
    if right>=1:
        if arr[mid_ele] == x:
            return mid_ele
        elif arr[mid_ele]<x:
            return binarySearch(arr, mid_ele+1, right, x)
        else:
            return binarySearch(arr, left, mid_ele-1, x)
    else:
        return -1


# Test array
arr = [ 2, 3, 4, 10, 40]
x = 40

result = binarySearch(arr, 0, len(arr ) -1, x)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print(f"Element is not present in array")

