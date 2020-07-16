"""
find the longest substring in the string
normal approach

Time complexity: O(N) square
space complexity:  O(N) square
"""


def find_longest_substring(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    max_length = 1
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 1
    # check for sub-string of length 2.
    start = 0
    # we can improve the below for loops
    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if string[i] == string[j]:
    #             start = i
    #             max_length = 2
    #             dp[i][j] = 1
    #         else:
    #             dp[i][j] = 0
    #         break

    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1
            if int(string[i] == string[j]) and dp[i + 1][j - 1]:
                dp[i][j] = 1
                if k > max_length:
                    start = i
                    max_length = k
            i += 1
        k += 1
    return string[start:start+max_length]


print(find_longest_substring("acaabaa"))
