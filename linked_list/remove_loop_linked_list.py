"""
https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

"""


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def detectAndRemoveLoop(self):
        if self.head is None or self.head.next is None:
            return self.head
        slow = self.head
        fast = self.head

        slow = slow.next
        fast = fast.next.next
        while fast is not None:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            slow = self.head
            while slow.next!=fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # Driver program
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)

    # Create a loop for testing
    llist.head.next.next.next.next.next = llist.head.next.next

    llist.detectAndRemoveLoop()

    print("Linked List after removing loop")
    llist.printList()
