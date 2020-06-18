"""
 find all possible palindromic substrings of a given string
"""


def find_palindromic_ss(inp_string):
    ans = set()
    N = len(inp_string)
    for each in range(2 * N - 1):
        left = each // 2
        right = left + (each % 2)
        print(left, right)
        while 0 <= left and right < N and inp_string[left] == inp_string[right]:
            print("correct", left, right)
            ans.add(inp_string[left:right + 1])
            left -= 1
            right += 1
    return ans


inp_string = "abaa"
print(find_palindromic_ss(inp_string))
