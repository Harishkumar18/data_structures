# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = head
        fast = head.next
        while slow is not None and slow.next is not None:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = slow.next
        return head
