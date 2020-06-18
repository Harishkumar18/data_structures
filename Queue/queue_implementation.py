"""
that this also means that enqueue will be O(n) and dequeue will be O(1).
"""

class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        return self.items


q1 = Queue()
print(q1.isempty())
print(q1.print_queue())
q1.enqueue(3)
q1.enqueue(2)
print(q1.print_queue())
q1.enqueue(1)
q1.enqueue(0)
print(q1.print_queue())
q1.dequeue()
print(q1.print_queue())
q1.dequeue()
print(q1.print_queue())
print(q1.isempty())
