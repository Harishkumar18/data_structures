""""
Description: Best time to buy and sell the stock challenge

did with help
result : achieved
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    def maxProfit2(self, prices):
        result = 0
        for i in range(len(prices) - 1):
            result += max(prices[i + 1] - prices[i], 0)
        return result


s1 = Solution()
res = s1.maxProfit2([7, 1, 5, 3, 6, 4])  # s1.maxProfit([1, 2, 3, 4, 5])
print(res)
