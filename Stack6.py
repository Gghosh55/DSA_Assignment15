def evaluatePostfixExpression(S):
    stack = []


    for char in S:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)


    return stack.pop()
postfix_expression = "231*+9-"
result = evaluatePostfixExpression(postfix_expression)
print(result)
