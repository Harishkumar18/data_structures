"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # remove all punctuations
        # change to lowercase
        # words count for each word not in banned set
        # return the most common word
        ban = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        return collections.Counter(word for word in words if word not in ban).most_common(1)[0][0]

    def mostCommonWord_wrong_soln(self, paragraph, banned):
        # brute force approach but not an correct solution
        # intitution: replace all chars except alphabets and space to empty space
        # convert it to lower case letters and convert it into list
        # get the len banned +1 most common words and remove the letters which is in banned
        # list so that we will be left with one word
        new_paragraph = re.sub("[^a-zA-Z ]+", "", paragraph)
        frequency_counter = collections.Counter(new_paragraph.lower().split(" "))
        freq_elem = [i[0] for i in frequency_counter.most_common(len(banned) + 1)]
        return list(set(freq_elem) - set(banned))[0]

