from coding_problems.decimal_to_binary import Stack as S


def postfixEval(postfix_string):
    evaluation_res = S()
    postfix_list = postfix_string.split()
    for token in postfix_list:
        if token in "0123456789":
            evaluation_res.push(token)
        else:
            operand2 = evaluation_res.pop()
            operand1 = evaluation_res.pop()
            calc = doMath(int(operand1), int(operand2), token)
            evaluation_res.push(str(calc))
    return evaluation_res.pop()



def doMath(op1, op2, operator):
    if operator == "+":
        return op1+op2
    elif operator == "-":
        return op1-op2
    elif operator == "/":
        return op1/op2
    else:
        return op1*op2



print(postfixEval('7 8 + 3 2 + /'))