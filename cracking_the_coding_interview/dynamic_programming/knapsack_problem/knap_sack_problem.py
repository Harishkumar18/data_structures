"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit out of the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Approach:
Brute force
The time complexity of the above algorithm is exponential O(2^n)
The space complexity is O(n)O(n).
"""


def solve_knapsack(profits, weights, capacity):
    return recursive_knapsack(profits, weights, capacity, 0)


def recursive_knapsack(profits, weights, capacity, currindex):
    if capacity <= 0 or currindex >= len(profits):
        return 0
    profit1 = 0
    if weights[currindex] <= capacity:
        profit1 = profits[currindex] + recursive_knapsack(profits, weights, capacity - weights[currindex], currindex + 1)
    profit2 = recursive_knapsack(profits, weights, capacity, currindex + 1)
    return max(profit1, profit2)


profits = [4, 5, 3, 7]
weights = [2, 3, 1, 4]
capacity = 5
print(solve_knapsack(profits, weights, capacity))
