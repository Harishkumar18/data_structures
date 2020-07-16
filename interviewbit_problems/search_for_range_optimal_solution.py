"""
optimal solution for search for range
O(log n)
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        # binary_search
        # for first and
        # last occurance
        def binary_search(A, B, flag):
            start = 0
            end = len(A) - 1
            result = -1

            while (start <= end):
                mid = int((start + end) / 2)
                if A[mid] == B:
                    result = mid
                    if flag:
                        end = mid - 1
                    else:
                        start = mid + 1
                elif A[mid] < B:
                    start = mid + 1
                elif B < A[mid]:
                    end = mid - 1
            return result

        # start_index using
        # binary search
        start_index = binary_search(A, B, True)

        # no start index found,
        # return [-1, -1]
        if start_index < 0:
            return [-1, -1]

        # end_index using
        # binary search
        end_index = binary_search(A, B, False)

        # return range
        return [start_index, end_index]