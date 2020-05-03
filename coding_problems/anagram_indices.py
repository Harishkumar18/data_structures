# to Solve the Anagram Indices Problem
# Given a word and a string S, find all starting indices in S which are anagrams of word.
# For example, given that word is “ab”, and S is “abxaba”, return 0, 3, and 4.

from collections import Counter


def isanagram(window, s):
    return Counter(window) == Counter(s)


def anagram_indices(word, s):
    result = []
    for i in range(len(s)-len(word)+1):
        window = s[i:i+len(word)]
        if isanagram(window, word):
            result.append(i)
    return result


if __name__ == '__main__':
    word = "ab"
    s = "abxaba"
    print(anagram_indices(word, s))