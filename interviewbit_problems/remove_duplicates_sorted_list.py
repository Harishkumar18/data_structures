"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3
"""


# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        if not A or A.next is None:
            return A
        res = ListNode(0)
        curr = res
        temp = A.val
        head = A.next
        while head:
            if head.val != temp:
                if temp:
                    curr.next = ListNode(temp)
                    curr = curr.next
                    temp = res.val
                else:
                    temp = head.val
            else:
                temp = None
            head = head.next
        return res

