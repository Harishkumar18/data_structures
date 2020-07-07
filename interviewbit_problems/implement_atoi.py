"""
implement atoi
"""


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        if len(A) == 0:
            return 0
        num_list = list(A.strip())
        sign = -1 if num_list[0] == "-" else 1
        if num_list[0] in ["-", "+"]:
            del num_list[0]
        i = 0
        n = len(num_list)
        ret = 0
        print(num_list)
        while i < n and num_list[i].isdigit():
            ret = ret * 10 + (ord(num_list[i]) - ord("0"))
            print("ret", ret)
            i += 1
        print("ret", ret)
        return max(-2 ** 31, min(ret * sign, 2 ** 31-1))


A = " -88297 248252140B12 37239U4622733246I218 9 1303 44 A83793H3G2 1674443R591 4368 7 97"
print(Solution().atoi(A))