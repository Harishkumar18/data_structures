"""

"""

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if not A or not B:
            return 0
        i = 0
        j = 0
        curr_index = None
        while i<len(A) and j<len(B):
            if A[i] == B[j]:
                if curr_index is None:
                    curr_index = i
                i+=1
                j+=1
            else:
                print("here", A[i], B[j])
                i+=1
                curr_index = None
        print("curr", curr_index)
        if j == len(B) and curr_index!=None:
            return curr_index
        return -1

A = "haridhrish"
B= "ris"
print(Solution().strStr(A, B))