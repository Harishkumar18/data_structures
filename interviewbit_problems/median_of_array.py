class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        merged_array = None
        if not A and not B:
            return float(0)
        if not A or not B:
            merged_array = A or B
        if not merged_array:
            merged_array = self.merge(A, B)
        print("merged arra", merged_array)
        n = len(merged_array)
        mid = n // 2
        print("mid", mid)
        if len(merged_array) % 2 == 0:
            return (merged_array[mid] + merged_array[mid - 1]) / 2
        else:
            return merged_array[mid]

    def merge(self, A, B):
        merged = [0] * (len(A) + len(B))
        i = 0
        k = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                merged[k] = A[i]
                i += 1
                k += 1
            else:
                merged[k] = B[j]
                k += 1
                j += 1
        while i < len(A) - 1:
            merged[k] = A[i]
            i += 1
            k += 1
        while j < len(B) - 1:
            merged[k] = B[j]
            j += 1
            k += 1
        return merged


A  = [ 0, 23 ]
B  = [  ]
print(Solution().findMedianSortedArrays(A, B))