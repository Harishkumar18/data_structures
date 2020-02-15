import itertools

class Solution:
    def countAndSay(self, n: int):
        s = "1"
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
            print("s here",s)
        return s

    def countAndSay2(self, n: int):
        s = "1"
        for _ in range(n - 1):
            v = ''
            for digit, group in itertools.groupby(s):
                count = len(list(group))
                v+="%i%s" %(count, digit)
            s = v
        return s


s1 = Solution()
inp_val = 4
print(s1.countAndSay2(inp_val))
