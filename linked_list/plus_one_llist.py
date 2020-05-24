from linked_list.linked_list_implementation import LinkedList
from linked_list.reverse_linked_list import reverseList


class Solution:
    def plus_one_ll(self, head):
        current = head
        carry = 1
        while current:
            current.data = (current.data + carry) % 10
            if current.data % 10 == 0:
                carry = 1
            else:
                carry = 0
            current = current.next
        return head


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(9)
    ll.insert(9)
    ll.insert(9)
    reverseList(ll)
    Solution().plus_one_ll(ll.head)
    reverseList(ll)
    ll.print_list()
