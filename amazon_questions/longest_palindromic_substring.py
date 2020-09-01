"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

TC: O(n^2)
"""


class Solution:
    # TC: o(n^2) in worst case
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # we need odd_palin to get the palindrome of odd length strings and
            # even_palin to get the palindrome of even length strings.
            # ex: aba will give aba and a as palindrome in odd and "" in even
            # abbd will give b in odd and bb in even
            odd_palin = self.helper(s, i, i)
            even_palin = self.helper(s, i, i + 1)
            odd_palin = ""
            longest = max(odd_palin, even_palin, longest, key=len)
        return longest

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

