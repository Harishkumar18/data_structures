from coding_problems.decimal_to_binary import Stack as S


def convert_infix_postfix(expression):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operator_stack = S()
    postfix_list = expression.split()
    result_list = []
    for token in postfix_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            result_list.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            # import pdb;
            # pdb.set_trace()
            top_elem = operator_stack.pop()
            while top_elem != "(":
                result_list.append(top_elem)
                top_elem = operator_stack.pop()
        else:
            while (not operator_stack.isempty()) and (prec[operator_stack.top()] >= prec[token]):
                result_list.append(operator_stack.pop())
            operator_stack.push(token)
    while not operator_stack.isempty():
        result_list.append(operator_stack.pop())
    final_res = ""
    if result_list:
        final_res = "".join(result_list)
    return final_res


# print(convert_infix_postfix("A * B + C * D"))
print(convert_infix_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
actual_result = "ABC*DEFG*-+-+"
expected_result = "A B + C * D E - F G + * -"