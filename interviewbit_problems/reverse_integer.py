"""
reverse a number with result overflow handled
"""

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if not A:
            return A
        sign = -1 if A<0 else 1
        A  = abs(A)
        reverse = ""
        while A:
            reverse+=str(A%10)
            A//=10
        if reverse > 2 ** 31 - 1:
            return 0
        return int(reverse)*sign

