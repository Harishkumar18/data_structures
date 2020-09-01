"""
https://leetcode.com/discuss/interview-question/370112

Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
"""


def find_distinct_char_brute_force(string, k):
    # brute force approach
    # TC: O(NK)
    n = len(string)
    result = set()
    for i in range(n - k + 1):
        if len(set(string[i:i + k])) == k:
            result.add(string[i:i + k])
    return list(result)


def find_distinct_char(string, k):
    if not string or k == 0:
        return []

    letters, res = {}, set()
    start = 0
    for i in range(len(string)):
        if string[i] in letters and letters[string[i]] >= start:
            start += 1
        letters[string[i]] = i
        if i - start + 1 == k:
            res.add(string[start:i + 1])
            start += 1
    return list(res)



# print(find_distinct_char_brute_force("abcabc", 3))
# print(find_distinct_char_brute_force("abacab", 3))
# print(find_distinct_char_brute_force("awaglknagawunagwkwagl", 4))


print(find_distinct_char("abcabc", 3))
print(find_distinct_char("abacab", 3))
print(find_distinct_char("awaglknagawunagwkwagl", 4))
