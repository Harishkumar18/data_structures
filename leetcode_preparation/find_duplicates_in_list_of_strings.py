"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt = collections.Counter(A[0])
        for s in A:
            cnt2 = collections.Counter(s)
            for k in cnt.keys():
                cnt[k] = min(cnt[k], cnt2[k])
        return cnt.elements()
    
 class Solution2:
 def commonChars(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())
