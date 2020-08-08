"""
Input: str = “((ng)ipm(ca))”
Output: camping
(gn ipm ac) - camping

"""


def reverse_string(inp_str):
    stack = []
    res = []
    for i in inp_str:
        if not i == ")":
            stack.append(i)
        else:
            while stack[-1] != "(":
                element = stack.pop()
                res.append(element)
            stack.pop()
            for each in res:
                stack.append(each)
            res = []
    return "".join(stack)


ans = reverse_string("((ng)ipm(((ca))))")
print(ans)


"""
cyware interview round 1

Input:

[1,1,2,2,3,3,4,4,7,8,8]
[1,1,2,2,3,4,4,6,6]


Input: str = “((ng)ipm(ca))”
Output: camping
(gn ipm ac) - camping


Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Given nums = [2, 7, 11, 15], target = 13,

Hash_map = {11:0,6:1,  }"""