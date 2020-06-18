from linked_list.linked_list_implementation import LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        rev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.data == slow.data:
            rev = rev.next
            slow = slow.next
        return not rev




ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(1)
# ll.print_list()
print(Solution().isPalindrome(ll.head))
