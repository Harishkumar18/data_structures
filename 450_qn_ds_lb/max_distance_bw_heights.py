"""
Minimise the maximum difference between heights [V.IMP]

https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/
"""


def get_difference(arr, k):
    arr.sort()

    ans = arr[-1] - arr[0]

    low = arr[0] + k
    high = arr[-1] - k

    for i in range(1, len(arr)-1):

        min_ele = arr[i] - k
        max_ele = arr[i] + k

        if min_ele >= low or max_ele <= high:
            pass

        if high - min_ele <= max_ele-low:
            low = min_ele
        else:
            high = max_ele

    return min(ans, high-low)


arr = [1,4,6,8]
k = 3
res = get_difference(arr, k)
print(res)