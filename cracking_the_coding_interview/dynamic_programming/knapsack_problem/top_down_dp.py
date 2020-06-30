"""
Memoization is when we store the results of all the previously solved sub-problems and return the results from memory
if we encounter a problem that has already been solved.

Since we have two changing values (capacity and currentIndex) in our recursive function knapsackRecursive(), we can
use a two-dimensional array to store the results of all the solved sub-problems. As mentioned above, we need to store
results for every sub-array (i.e. for every possible index ‘i’) and for every possible capacity ‘c’.

Time and Space complexity #
Since our memoization array dp[profits.length][capacity+1] stores the results for all subproblems, we can conclude
that we will not have more than N*CN∗C subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity).
 This means that our time complexity will be O(N*C)O(N∗C).

The above algorithm will use O(N*C) space for the memoization array. Other than that we will use O(N) space
for the recursion call-stack. So the total space complexity will be O(N*C + N), which is asymptotically
equivalent to O(N*C).
"""


def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for i in range(capacity+1)] for j in range(len(weights))]
    return recursive_knapsack(dp, profits, weights, capacity, 0)


def recursive_knapsack(dp, profits, weights, capacity, currindex):
    if capacity <= 0 or currindex >= len(profits):
        return 0
    if dp[currindex][capacity]!=-1:
        return dp[currindex][capacity]
    profit1 = 0
    if weights[currindex] <= capacity:
        profit1 = profits[currindex] + recursive_knapsack(dp, profits, weights, capacity - weights[currindex], currindex + 1)
    profit2 = recursive_knapsack(dp, profits, weights, capacity, currindex + 1)
    dp[currindex][capacity] = max(profit1, profit2)
    return dp[currindex][capacity]


profits = [4, 5, 3, 7]
weights = [2, 3, 1, 4]
capacity = 5
print(solve_knapsack(profits, weights, capacity))