# single node of singly linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for linked list
    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def delete_linked_list(self):
        current = self.head
        while current:
            del current.data
            self.head = current.next
            current = current.next

    # print elements of the linked list
    def print_list(self):
        if not self.head:
            return None
        current = self.head
        while current:
            print(current.data)
            current = current.next


# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# # ll.insert(3)
# # ll.insert(4)
# # ll.insert(5)
# ll.print_list()
# ll.delete_linked_list()
# print("result after deleting linked list")
# ll.print_list()
# creating first node
# n1 = Node(3)
# print(n1.data)
# print(n1.next)

# creating linked list
# ll = LinkedList()
# ll.head = Node(3)
# print(ll.head.data)
# print(ll.head.next)