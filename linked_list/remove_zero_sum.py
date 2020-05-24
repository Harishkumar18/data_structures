"""
Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.


(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Note: Implemented this in leetcode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printlist(head):
    current = head
    while current:
        print(current.val)
        current = current.next
    print(f"Done")


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        return dummy


inp_list = [1,2,-3,3,1]
res = Solution().removeZeroSumSublists(ListNode())
printlist(res)