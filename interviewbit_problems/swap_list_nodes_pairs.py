"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = ListNode(None)
        head.next = A
        prev = head
        curr = A

        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev = curr
            curr = curr.next

        return head.next


class SolutionRecursive:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second


class SolutionBYModifyingNodesValue:
    def swapPairs(self, A):
        n=A
        while(n!=None and n.next!=None):
            temp=n.next
            n.val,temp.val=temp.val,n.val
            n=temp.next
        return A

    def swapPairs(self, head):
        root = ListNode(0)
        root.next = head
        cur = root.next
        old = head
        flag = False
        while cur.next:
            if flag:
                tmp = cur.next
                cur.next = tmp2
                tmp2.next = tmp
                old.next = cur
                cur = cur.next
            else:
                tmp2 = cur
            flag = not flag

        return root.next

