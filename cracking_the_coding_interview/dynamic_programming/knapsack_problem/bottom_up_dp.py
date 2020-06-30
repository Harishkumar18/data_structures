"""
This means that dp[i][c] will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items.

So, for each item at index ‘i’ (0 <= i < items.length) and capacity ‘c’ (0 <= c <= capacity), we have two options:

Exclude the item at index ‘i’. In this case, we will take whatever profit we get from the sub-array excluding this
item => dp[i-1][c]
Include the item at index ‘i’ if its weight is not more than the capacity. In this case, we include its profit plus
whatever profit we get from the remaining capacity and from remaining items => profit[i] + dp[i-1][c-weight[i]]

Finally, our optimal solution will be maximum of the above two values:

    dp[i][c] = max (dp[i-1][c], profit[i] + dp[i-1][c-weight[i]])

The above solution has the time and space complexity of O(N*C), where ‘N’ represents total items and ‘C’ is the
maximum capacity.
"""


def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity<=0 or len(weights)!=n:
        return 0

    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity+1):
        if weights[0] <=c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i]<=c:
                profit1 = dp[i-1][c-weights[i]] + profits[i]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    return dp[n-1][capacity]

profits = [4, 5, 3, 7]
weights = [2, 3, 1, 4]
capacity = 5
print(solve_knapsack(profits, weights, capacity))