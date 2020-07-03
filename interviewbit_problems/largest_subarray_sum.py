"""
find the largest subarray sum
"""


def find_sum(A):
    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum


print(find_sum([-2, 1, -3, 4, -1, 2,1]))