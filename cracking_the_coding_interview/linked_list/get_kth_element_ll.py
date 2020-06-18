from linked_list.linked_list_implementation import LinkedList


class Solution:
    def kthelement(self, head, k):
        if not head:
            return None
        p1 = head
        p2 = head
        for _ in range(k):
            if not p1:
                return None
            p1 = p1.next
        while p1:
            p2 = p2.next
            p1 = p1.next
        return p2


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
# ll.insert(6)
# ll.print_list()
res = Solution().kthelement(ll.head, 3)
print(res.data)