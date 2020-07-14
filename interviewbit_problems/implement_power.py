"""

"""


class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if not x or not d:
            return 0
        if not n:
            return 1 % d
        result = 1
        base = x

        while n > 0:
            if n % 2 == 0:
                base = (base * base) % d
                n /= 2
            else:
                result = (result * base) % d
                n -= 1
        if result < 0:
            result = (result + d) % d

        return result


print(Solution().pow(-3, 3, 4))