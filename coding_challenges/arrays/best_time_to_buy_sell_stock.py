""""
Description: Best time to buy and sell the stock challenge

result : didn't achieve all the conditions given in the problem
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for each in range(len(prices)):
            previous_profit = 0
            for each_next in range(each + 1, len(prices)):
                if prices[each_next] < prices[each]:
                    continue
                current_profit = prices[each_next] - prices[each]
                if current_profit > previous_profit:
                    previous_profit = current_profit
                else:
                    break
            total_profit += previous_profit
        return total_profit


s1 = Solution()
res = s1.maxProfit([7, 1, 5, 3, 6, 4])
res1 = s1.maxProfit([1, 2, 3, 4, 5])
res2 = s1.maxProfit([7, 6, 4, 3, 1])
print(res)
print(res1)
print(res2)
