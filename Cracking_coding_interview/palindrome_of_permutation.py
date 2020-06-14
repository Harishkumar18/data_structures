"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""


def find_palindrome_in_permutations(string1):
    string1 = string1.lower()
    character_count = {}
    for each in string1:
        if each not in character_count:
            character_count[each] = 1
        else:
            character_count[each]+=1
    count = 0
    for value in character_count.values():
        if value == 1:
            count+=1
    if count>1:
        return False
    return True


print(find_palindrome_in_permutations("TactCoa"))