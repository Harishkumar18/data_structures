# Python program to delete M nodes after N nodes

# Node class
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

        # Utility function to prit the linked LinkedList

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,)
            temp = temp.next

    def skipMdeleteN(self, M, N):
        pass


# Driver program to test above function


# Create following linked list
# 1->2->3->4->5->6->7->8->9->10
llist = LinkedList()
M = 2
N = 3
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("M = %d, N = %d\nGiven Linked List is:" % (M, N))
llist.printList()
print(llist.skipMdeleteN(M, N))

print("\nLinked list after deletion is")
llist.printList()