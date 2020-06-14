"""
Write a method to replace all spaces in a string with '%20'.
"""


def modify_string(inp_str):
    new_str = ""
    for ch in inp_str:
        if ch.isspace():
            new_str+="%20"
        else:
            new_str+=ch
    return new_str

print(modify_string("hari sh k"))