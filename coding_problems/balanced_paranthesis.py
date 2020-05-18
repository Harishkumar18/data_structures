"""
https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimpleBalancedParentheses.html
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1]

    def show_stack(self):
        return self.items

    def isempty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)


def find_balance_paranthesis(inp_str, stack):
    """
    Description: applies only for one type brackets
    """
    for each in inp_str:
        if each == "(":
            stack.push(each)
        elif each == ")" and not stack.isempty():
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    return False


# inp_str = "(())(())"
# stack = Stack()
# print(find_balance_paranthesis(inp_str, stack))

def matches(close, open):
    opens = "([{"
    closes = ")]}"
    return closes.index(close) == opens.index(open)


def check_parantheses(inp_str):
    stack = Stack()
    balanced = True
    index = 0
    while index < len(inp_str) and balanced:
        element = inp_str[index]
        if element in "({[":
            stack.push(element)
        else:
            if stack.isempty():
                balanced = False
            else:
                if matches(element, stack.top()):
                    stack.pop()
                else:
                    balanced = False
        index += 1
    if len(stack) == 0 and balanced:
        return True
    else:
        return False


inp_str = "(()){}(())}"
print(check_parantheses(inp_str))
