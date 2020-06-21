from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, char in enumerate(shortest):
            for others in strs:
                if others[index]!=char:
                    print("shortest", shortest[:index])
                    return shortest[:index]
        return shortest



print(Solution().longestCommonPrefix(["fl","flower","flow","felight"]))