"""
You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log, letter_log = [], []
        for log in logs:
            if log.split(" ")[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)
        letter_log.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return letter_log + digit_log

    def reorderlogfiles_using_heap(self, logs):
        letter, digit, heap = [], [], []
        for log in logs:
            tail = log.split(" ", 1)[1]
            if tail[0].isalpha():
                heappush(heap, (tail, log))
            else:
                digit.append(log)
        while heap:
            letter.append(heappop(heap)[1])
        return letter + digit
