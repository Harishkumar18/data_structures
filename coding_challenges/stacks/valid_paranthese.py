class Solution:
    def isValid(self, s: str):
        stack = []
        valid = False
        if not s:
            valid = True
            return valid
        for each in s:
            if each in ['(', '[', '{']:
                stack.append(each)
            else:
                if not stack:
                    return False
                top_element = stack.pop()
                print("te",top_element)
                if each == '}' and top_element != '{':
                    return False
                elif each == ']' and top_element != '[':
                    return False
                elif each == ')' and top_element != '(':
                    return False
        if not stack:
            valid = True
        return valid



s1 = Solution()
inp_str = "]"
print(s1.isValid(inp_str))