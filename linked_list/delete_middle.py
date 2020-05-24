"""
https://practice.geeksforgeeks.org/problems/delete-middle-of-linked-list/1
"""
from linked_list.linked_list_implementation import LinkedList


class Solution:
    def middleNode(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)

Solution().middleNode(ll.head)
ll.print_list()
# print(res.data)
