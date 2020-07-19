"""
"Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL."

TC: O(n)
SC: O(1)

"Approach:
here b is times of rotate(right rotate)
1) if not head or not B return head
2) get the length of the linked list
3) do modulo operation for B with length
4) subtract b from length then we will come to the end node
5) Change the next of the kth node to NULL.
6) Change the next of the last node to the previous head node.
7) Change the head to (k+1)th node."
"""


# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, head, B):
        if not head or not B:
            return head
        curr = prev = head
        length = 1
        while head.next:
            head = head.next
            length += 1
        B = B % length
        if B == 0:
            return curr
        i = 1
        while i < (length - B):
            curr = curr.next
            i += 1
        last = curr
        new_head = curr.next
        while curr.next:
            curr = curr.next
        curr.next = prev
        last.next = None
        return new_head
