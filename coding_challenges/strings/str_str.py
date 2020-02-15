class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def strStr2(self, haystack: str, needle: str):
        if not needle:
            return 0
        end_point = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+end_point] == needle:
                return i
        return -1

s1 = Solution()
haystack, needle = "missisippi", "isippi"
print(s1.strStr2(haystack, needle))