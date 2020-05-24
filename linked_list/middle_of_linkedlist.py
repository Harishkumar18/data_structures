from linked_list.linked_list_implementation import LinkedList


class Solution:
    def middleNode(self, head):
        if not head:
            return None
        slow = head
        fast = head.next
        while fast is not None:
            slow = slow.next
            if not fast.next:
                return slow
            fast = fast.next.next
        return slow


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
# ll.print_list()
res = Solution().middleNode(ll.head)
print(res.data)
