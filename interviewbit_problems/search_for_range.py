"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]

Time complexity: O(log n)
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        start = 0
        end = len(A)
        while start < end:
            if start >= end:
                break
            mid = start + (end - start) // 2
            if A[mid] == B:
                start = self.find_starting_index(A, B, mid, start)
                end = self.find_ending_index(A, B, mid, end)
                return [start, end]
            elif A[mid] < B:
                start = mid + 1
            else:
                end = mid
        return [-1, -1]

    def find_starting_index(self, arr, element, index, limit):
        i = index
        while i >= limit and arr[i] == element:
            i -= 1
        return i + 1

    def find_ending_index(self, arr, element, index, limit):
        i = index
        while i < limit and arr[i] == element:
            i += 1
        return i - 1


# TC1
# A = [5, 7, 7, 8, 8, 10]
# B = 8
# TC2:
# A = [5, 17, 100, 111]
# B = 3
# TC3
# A = [5, 6, 7, 7, 8, 8, 10]
# B = 8
# TC4
# A = [5, 7, 7, 8, 8, 8, 10]
# B = 7
# TC5
# A = [5, 6, 7, 7, 8, 9, 10]
# B = 8
# TC6
A = [1]
B = 1
print(Solution().searchRange(A, B))
