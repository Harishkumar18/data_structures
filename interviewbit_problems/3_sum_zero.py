"""

"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if not A:
            return A
        A.sort()
        print("sorted", A)
        result = []
        i = 0
        n = len(A)
        # while i<n:
        for i in range(n-1):
            pointer1 = i + 1
            pointer2 = n - 1
            while pointer1< pointer2:
                if (A[i] + A[pointer1] + A[pointer2]) == 0:
                    result += [A[i], A[pointer1], A[pointer2]],
                    pointer1+=1
                    pointer2-=1
                elif (A[i] + A[pointer1] + A[pointer2]) < 0:
                    pointer1 += 1
                else:
                    pointer2 -= 1
        return result


# A = [0, 1, -1, 2, -4, -1]
A = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
print(Solution().threeSum(A))
