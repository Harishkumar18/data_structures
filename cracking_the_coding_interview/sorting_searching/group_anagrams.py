"""
Write a method to sort an array ot strings so that all tne anagrnms are next to
each other.
"""
from collections import defaultdict


def group_anagrams(inp_list):
    final_res = []
    group_dict = defaultdict(list)
    for each in inp_list:
        group_dict["".join(sorted(each))].append(each)
    for key in group_dict:
        final_res.append([i for i in group_dict[key]])
    return final_res


print(group_anagrams(["god", "tea", "cat", "dog", "ate", "act", "eat"]))
