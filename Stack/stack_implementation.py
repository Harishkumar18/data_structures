"""
 the append and pop() operations were both O(1).
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def show_stack(self):
        return self.items

    def isempty(self):
        return self.items == []


# s1 = Stack()
# print(s1.isempty())
# s1.push(4)
# s1.push(3)
# s1.push(2)
# s1.push(1)
# print(s1.top())
# print(s1.show_stack())
# s1.pop()
# s1.pop()
# print(s1.top())
# print(s1.show_stack())
