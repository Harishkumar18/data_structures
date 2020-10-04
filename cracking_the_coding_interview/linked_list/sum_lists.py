"""

"""
from cracking_the_coding_interview.linked_list.partition_linked_list import ListNode


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = n = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            val1 = l1.val
            l1 = l1.next
        else:
            val1 = 0
        if l2:
            val2 = l2.val
            l2 = l2.next
        else:
            val2 = 0
        carry, val = divmod(val1 + val2 + carry, 10)
        n.next = ListNode(val)
        n = n.next

    return root.next


234
45