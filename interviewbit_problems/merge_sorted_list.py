"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""


# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A and not B:
            return A or B
        if not A or not B:
            return A or B
        res = curr = ListNode(0)
        while A and B:
            if A.val < B.val:
                res.next = ListNode(A.val)
                res = res.next
                A = A.next
            else:
                res.next = ListNode(B.val)
                res = res.next
                B = B.next
        while A:
            res.next = ListNode(A.val)
            res = res.next
            A = A.next
        while B:
            res.next = ListNode(B.val)
            res = res.next
            B = B.next
        return curr.next


class SolutionOptimized:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A and not B:
            return A or B
        if not A or not B:
            return A or B
        start = end = ListNode(0)
        while A and B:
            if A.val < B.val:
                end.next = A
                A = A.next
            else:
                end.next = B
                B = B.next
            end = end.next
        if A:
            end.next = A
        elif B:
            end.next = B
        return start.next
