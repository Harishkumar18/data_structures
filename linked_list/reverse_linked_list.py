"""
https://www.pythoncentral.io/reverse-singly-linked-list/
"""
from linked_list.linked_list_implementation import LinkedList


def reverseList(linked_list):
    """Iterative solution"""
    prev = None
    current = linked_list.head
    next_ele = current.next
    while current:
        current.next = prev
        prev = current
        current = next_ele
        if next_ele:
            next_ele = next_ele.next
    linked_list.head = prev


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print(f"Linked List")
    print(ll.print_list())
    print(f"reversed linked list")
    reverseList(ll)
    ll.print_list()

