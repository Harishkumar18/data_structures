from Stack.stack_implementation import Stack


def perform_operation(input_string):
    s = Stack()
    for i in range(len(input_string)):
        print(input_string[i])
        if input_string[i].isdigit():
            s.push(input_string[i])
        else:
            a = s.pop()
            b = s.pop()
            res =str(eval(b + input_string[i] + a))
            s.push(res)
    return s.top()


print(perform_operation("12+3*66*+"))