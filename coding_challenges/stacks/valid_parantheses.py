class Solution:
    def isValid(self, s: str):
        mapping = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        if not s:
            return True
        stack = []
        for each in s:
            if each in mapping:
                stack.append(each)
            else:
                if stack and each == mapping[stack.pop()]:
                    continue
                else:
                    return False
        return True if not stack else False

s1 = Solution()
inp_str = "]"
print(s1.isValid(inp_str))
