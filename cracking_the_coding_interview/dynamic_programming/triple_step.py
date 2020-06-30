"""
triple step using 1 step, 2 step and 3 step using normal recursion
"""


def count_no_ways(n):
    """Normal iterative approach
    TC: O(3 power n)
    SC: O(1)"""
    if n<0:
        return 0
    if n == 0:
        return 1
    return count_no_ways(n-1)+ count_no_ways(n-2)+ count_no_ways(n-3)


def countways(n):
    """
    Dynamic programming concepts
    Type: Bottom up approach
    TC: O(n)
    SC: O(n)
    """
    result = [0] * (n+1)
    result[0] = 1
    result[1] = 1
    result[2] = 2
    for i in range(3, n+1):
        result[i] = result[i-1]+result[i-2]+result[i-3]
    return result[n]


def count_ways(n, result):
    if n <=0:
        return result.get(n, 0)
    if n not  in result:
        result[n] = count_ways(n-1, result)+count_ways(n-2, result)+count_ways(n-3, result)
        print(result)
    return result[n]


def countways_td_approach(n):
    """
    Dynamic programming concepts
    Type: TOP Down approach
    TC: O(n)
    SC: O(n)
    """
    result = {0: 1, 1:1}
    return count_ways(n, result)


# recursive approach
print(count_no_ways(10))
# top down approach
print(countways(10))
# bottom up approach
print(countways_td_approach(6))