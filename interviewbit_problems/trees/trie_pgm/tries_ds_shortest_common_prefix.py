"""
trie ds
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self._get_node()

    def _get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch)-ord('a')

    def insert(self, key):
        pointer = self.root

        for ch in key:
            index = self._char_to_index(ch)
            if not pointer.children[index]:
                pointer.children[index] = [self._get_node(), 1]
            else:
                new_pointer, curr_count = pointer.children[index]
                pointer.children[index] = [new_pointer, curr_count + 1]
            pointer, _ = pointer.children[index]

        pointer.isEndOfWord = True

    def search(self, key):
        pointer = self.root
        for ch in key:
            index = self._char_to_index(ch)
            if not pointer.children[index]:
                return False
            else:
                pointer, count = pointer.children[index]

        if pointer != None and pointer.isEndOfWord == True:
            return 1
        else:
            return 0

    def unique_prefix(self, key):
        pointer = self.root
        uni_pref = ""
        for ch in key:
            index = self._char_to_index(ch)
            pointer, count = pointer.children[index]
            if count == 1:
                return (uni_pref + ch)
            else:
                uni_pref = uni_pref + ch
        return ""


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):

        # Trie object
        t = Trie()
        # Construct trie
        for key in A:
            t.insert(key)
        output = []
        for key in A:
            output.append(t.unique_prefix(key))
        return output

inp_words = ["zebra", "dog", "duck", "dove"]
print(Solution().prefix(inp_words))
