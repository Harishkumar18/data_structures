"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.
"""


class MinStack:
    def __init__(self):
        self.items = []

    # @param x, an integer
    def push(self, x):
        currmin = self.getMin()
        if currmin == -1 or x < currmin:
            currmin = x
        self.items.append((x, currmin))

    # @return nothing
    def pop(self):
        if self.items:
            self.items.pop()

    # @return an integer
    def top(self):
        if self.items:
            return self.items[-1][0]
        return -1

    # @return an integer
    def getMin(self):
        if not self.items:
            return -1
        return self.items[-1][1]

