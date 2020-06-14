"""
1.5 One Away:
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check ifthey are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def find_one_edit(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n2-n1 > 1:
        return False
    if n1 == n2:
        count_diff = 0
        for ch in range(n1):
            if s1[ch]!=s2[ch]:
                count_diff+=1
        if count_diff<2:
            return True

    if n1+1==n2:
        ins_pos = 0
        for i in range(n1):
            if s1[i]!=s2[i]:
                ins_pos = i
                break
        else:
            return True
        if s1[:ins_pos] == s2[:ins_pos] and s1[ins_pos:] == s2[ins_pos+1:]:
            return True

    if n1 == n2+1:
        del_pos = 0
        for i in range(n2):
            if s2[i]!=s1[i]:
                del_pos = i
                break
        else:
            return True
        if s1[:del_pos] == s2[:del_pos] and s1[del_pos+1:] == s2[del_pos:]:
            return True
    return False


print(find_one_edit("pale", "sale"))

print(find_one_edit("abcde", "abcd"))

print(find_one_edit("helo", "hello"))

print(find_one_edit("hello", "hellonp"))

print(find_one_edit("helo", "malo"))