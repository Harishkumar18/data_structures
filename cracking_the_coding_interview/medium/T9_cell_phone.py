"""
T9: On old cell phones, users typed on a numeric keypad and the phone would provide a list of
words that matched these numbers. Each digit mapped to a set of O - 4 letters. Implement an algorithm
to return a list of matching words, given a sequence of digits. You are provided a list of valid
words (provided in whatever data structure you'd like). The mapping is shown in the diagram below:
Input:
Output:
8733
tree, used
"""


hashtable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


def printwordsutil(number, curr, output, n):
    if curr == n:
        print(output)
        return

    for i in range()


def printwords(number):
    printwordsutil(number, 0, [], len(number))

number = [8, 7, 3, 3]
print(printwords(number))