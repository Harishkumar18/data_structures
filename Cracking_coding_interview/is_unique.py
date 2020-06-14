"""
"1) solving problem Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?"
"""


def find_unique(inp_str):
    if len(inp_str)>128:
        return False
    boolean_char = [False for i in range(128)]
    for character in range(len(inp_str)):
        if boolean_char[ord(inp_str[character])]:
            return False
        boolean_char[ord(inp_str[character])] = True
    return True


inp_strs = ["harish", "kumar", "", "0123", "01231"]
for inp_str in inp_strs:
    print(find_unique(inp_str))