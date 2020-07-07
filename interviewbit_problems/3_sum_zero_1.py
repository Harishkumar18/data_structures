def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()
    res = []
    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):

            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                # print(x, arr[l], arr[r])
                res += [arr[x], arr[l], arr[r]],
                l += 1
                r -= 1
                # found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    return res
    # Driven source


# arr = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
# n = len(arr)
# res = findTriplets(arr, n)
# print(res)
# # [-5 0 5 ] [-5 1 4 ] [-4 -1 5 ] [-4 0 4 ] [-4 1 3 ] [-3 -2 5 ] [-3 -1 4 ] [-3 0 3 ] [-2 -1 3 ] [-2 1 1 ] [-1 0 1 ] [0 0 0 ]]


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if not A:
            return A
        A.sort()
        result = set(())
        i = 0
        n = len(A)
        for i in range(0, n-1):
            pointer1 = i + 1
            pointer2 = n - 1
            while pointer1< pointer2:
                if (A[i] + A[pointer1] + A[pointer2]) == 0:
                    result.add((A[i], A[pointer1], A[pointer2]))
                    pointer1 += 1
                    pointer2 -= 1
                elif (A[i] + A[pointer1] + A[pointer2]) < 0:
                    pointer1 += 1
                else:
                    pointer2 -= 1
        return list(result)


A = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
res = Solution().threeSum(A)
print(res)
# [-5 0 5 ] [-5 1 4 ] [-4 -1 5 ] [-4 0 4 ] [-4 1 3 ] [-3 -2 5 ] [-3 -1 4 ] [-3 0 3 ] [-2 -1 3 ] [-2 1 1 ] [-1 0 1 ] [0 0 0 ]]