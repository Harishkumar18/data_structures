"""
shortest unique path using trie
"""

from collections import defaultdict


class Solution:
    def prefix(self, words):
        prefixes = defaultdict(int)
        for word in words:
            for i in range(1, len(word)):
                prefixes[word[:i]] += 1
        output = []
        for word in words:
            result = word
            for i in range(1, len(word)):
                pref = word[:i]
                if prefixes[pref] == 1:
                    result = pref
                    break
            output.append(result)
        return output


words_list = ["dog", "dove", "duck", "zebra"]
print(Solution().prefix(words_list))
