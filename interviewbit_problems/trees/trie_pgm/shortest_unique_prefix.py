"""
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
"""


class Trie:
    def __init__(self):
        self.letters = {}

    def addstring(self, s):
        letters = self.letters
        for ch in s:
            if ch not in letters:
                letters[ch] = {"freq": 1}
            else:
                letters[ch]["freq"] += 1
            letters = letters[ch]
        letters["*"] = True

    def generateprefix(self, s):
        prefix = []
        letters = self.letters
        for c in s:
            prefix.append(c)
            if letters[c]["freq"] == 1:
                break
            letters = letters[c]
        return "".join(prefix)


class Solution:
    def prefix(self, words):
        trie_obj = Trie()
        for word in words:
            trie_obj.addstring(word)
        ans = []
        for each in words:
            prefix = trie_obj.generateprefix(each)

            ans.append(prefix)
        return ans


inp_words = ["zebra", "dog", "duck", "dove"]
print(Solution().prefix(inp_words))
