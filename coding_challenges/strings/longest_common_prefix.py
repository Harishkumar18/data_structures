class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for index, char in enumerate(shortest):
            for others in strs:
                if others[index]!=char:
                    return shortest[:index]
        return shortest

s1 = Solution()
inp_val = ['flower', 'flow', 'flownght']
print(s1.longestCommonPrefix(inp_val))