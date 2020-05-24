# A linked list node
class Node:
    def __init__(self, data, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down


def printlist(head):
    print("printing all elements")
    current = head
    while current:
        print(current.data, end="->")
        current = current.down
    print("\n")
    print("done printing all elem")


def createhorizontallist(head, A):
    for key in A:
        head = Node(key, head)
    return head


def createverticallist(head, A):
    for key in A:
        head = Node(key, down=head)
    return head


# function which will take two linked list merge and provide one sorted list
def sortedmerge(a, b):
    if a is None:
        return b
    elif b is None:
        return a
    if a.data <= b.data:
        result = a
        result.down = sortedmerge(a.down, b)
    else:
        result = b
        result.down = sortedmerge(a, b.down)
    return result


# flatten the list
def flatten(head):

    if head is None:
        return head

    sorted = sortedmerge(head, flatten(head.next))
    head.next = None
    return sorted


first = [8, 6, 4, 1]
second = [7, 3, 2]
third = [9, 5]
fourth = [12, 11, 10]
head = createverticallist(None, first)
head.next = createverticallist(head, second)
head.next.next = createverticallist(head.next, third)
head.next.next.next = createverticallist(head.next.next, fourth)
# printlist(head)
flatten(head)
