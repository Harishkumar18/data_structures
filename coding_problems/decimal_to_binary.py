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

    def __len__(self):
        return len(self.items)


def divide_by_2(decimal_value):
    if not decimal_value > 0:
        return -1
    s = Stack()
    while decimal_value:
        remainder = decimal_value % 2
        s.push(remainder)
        decimal_value = decimal_value // 2
    binary_no = ""
    while not s.isempty():
        binary_no = binary_no + str(s.pop())
    return binary_no


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    print(remstack.show_stack())
    newString = ""
    while not remstack.isempty():
        newString = newString + digits[remstack.pop()]

    return newString

# print(baseConverter(233, 16))
