"""
Move all the negative elements to one side of the array
"""


def move_negative_nos(arr):
    neg = 0
    pos = len(arr)-1
    while neg <= pos:
        if arr[neg] < 0 :
            neg += 1
        else:
            arr[neg], arr[pos] = arr[pos], arr[neg]
            pos -= 1
    return arr


arr = [9, -8, 5, 0, -4, -6]
res = move_negative_nos(arr)
print(res)