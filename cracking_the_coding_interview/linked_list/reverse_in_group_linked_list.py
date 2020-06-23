# TODO: implement again or do from scratch
# A linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Helper function to print linked list starting from current node
    def print(self):
        ptr = self
        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next

        print("None")


# Function to reverse every group of k nodes in given linked list
def reverseInGroups(head, k):
    # base case
    if head is None:
        return None

    # start with current node
    current = head

    # reverse next k nodes
    prev = None
    count = 0

    # Iterate through the list and move/insert each node to the
    # front of the result list (like a push of the node)
    while current and count < k:
        count = count + 1

        # tricky: note the next node
        next = current.next

        # move the current node onto the result
        current.next = prev

        # update previous to current node
        prev = current

        # move to next node in the list
        current = next

    # recur for remaining nodes
    head.next = reverseInGroups(current, k)

    # important - return previous (to link every group of k nodes)
    return prev


if __name__ == '__main__':

    head = None
    for i in reversed(range(8)):
        head = Node(i + 1, head)

    head = reverseInGroups(head, 3)
    head.print()
