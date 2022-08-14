class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_mapp = {'(': ')', '{': '}', '[': ']'}
        for ch in s:
            if ch in valid_mapp:
                stack.append(ch)
            elif ch in valid_mapp.values():
                if stack == [] or ch != valid_mapp[stack.pop()]:
                    return False
        return stack == []
