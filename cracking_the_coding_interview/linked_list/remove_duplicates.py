'''
The time complexity for removing duplicate nodes is O(n) because, I used set() which stores unique nodes and searching takes O(1).
So, O(n) is for traversing the linked list where n is size of linked list.
And the space complexity is O(n) to store n keys in set().
'''


class Node():
    """Single node of singly linked list"""

    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __str__(self):
        return str(self.data)


class LinkedList():
    """Create singly linked list by passing the list to the constructor"""
    def __init__(self, linkedList):
        self.head = None
        self.add(linkedList)

    def add(self, linkedList):
        #reversing ensures that the data is passed in the same sequence as it`s present in the list
        #the function reversed() reverses the list on the fly
        #here the time is O(n) where n is number of elements in the list
        for data in reversed(linkedList):
            node = Node(data)
            node.nextNode = self.head
            self.head = node

    def printList(self):
        #print also takes O(n) time
            node = self.head
            if node is not None:
                print(node)
                node = node.nextNode

            while node:
                print(">", node)
                node = node.nextNode
            print("\n")

def removeDuplicates(linkedList):
    prev = linkedList.head
    curr = prev.nextNode
    keys = {prev.data}
    while curr:
        data = curr.data
        if data in keys:
            prev.nextNode = curr.nextNode
            curr = curr.nextNode
        else:
            keys.add(data)
            prev = curr
            curr = curr.nextNode

    print("After removing the duplicates:")
    linkedList.printList()

list1 = [1, 2, 5, 1, 3, 5, 4]
list2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f', 'b']
list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']

l = LinkedList(list1)
# l.printList()
removeDuplicates(l)

# l = LinkedList(list2)
# l.printList()
# removeDuplicates(l)
#
# l = LinkedList(list3)
# l.printList()
# removeDuplicates(l)
