"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        size = len(coins)
        arr = [[0] * (amount + 1) for x in range(size + 1)]

        for i in range(size + 1):
            arr[i][0] = 0

        for i in range(1, size + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = 1 + arr[i][j - coins[i - 1]]
        return arr[size][amount] if not 0 else -1 