"""
"Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
If n is greater than the size of the list, remove the first node of the list."

"There are 2 approaches :
1) Find out the length of the list in one go. Then you know the number of node to be removed. Traverse to the node and remove it.
2) Make the first pointer go n nodes. Then move the second and first pointer simultaneously. This way, the first pointer is always ahead of the
second pointer by n nodes. So when first pointer reaches the end, you are on the node to be removed."
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
    def removeNthFromEnd(self, A, B):
        if not A or A.next is None:
            return None
        start = end = A
        i = 1
        while end and end.next:
            end = end.next
            i += 1
        to_delete = i - B
        if to_delete <= 0:
            return start.next
        i = 0
        while i < (to_delete - 1):
            A = A.next
            i += 1
        A.next = A.next.next
        return start


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class SolutionOptimized:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A:
            return A
        slow = fast = A
        for _ in range(B):
            if fast.next:
                fast = fast.next
            else:
                return A.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return A

