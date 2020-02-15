
class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0: return 0
        num_list = list(str.strip())
        sign = -1 if num_list[0] == '-' else 1
        if num_list[0] in ['-', '+']: del num_list[0]
        ret, i = 0, 0
        while i<len(num_list) and num_list[i].isdigit():
            ret = ret*10 + (ord(num_list[i])- ord('0'))
            i+=1
        return max(-2**31, min(ret*sign, 2**31-1))

s1 = Solution()
str = "-124-"
print(s1.myAtoi(str))
