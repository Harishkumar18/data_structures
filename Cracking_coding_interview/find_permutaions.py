"""
"2) Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other."
"""


def char_frequency(string1):
    character_count = {}
    for each in string1:
        if each in character_count:
            character_count[each] += 1
        else:
            character_count[each] = 1
    return character_count


def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for each in dict1:
        if dict1[each] != dict2[each]:
            return False
    return True


def check_permutations(string1, string2):
    char_count1 = char_frequency(string1)
    char_count2 = char_frequency(string2)
    return compare_dicts(char_count1, char_count2)


print(check_permutations("abc", "bcad"))
