
expr = "(((1.1 * 2) + 3.3) / 5)"


def infix_eval(expression):
    stack = []
    num = ""
    for c in expression:
        if c in "1234567890.":
            num += c
            continue

        if num != "":
            stack.append(float(num))
            num = ""

        if c in "+-*/":
            stack.append(c)
        elif c == ')':
            num2 = stack.pop()
            op = stack.pop()
            num1 = stack.pop()
            match op:
                case "+":
                    stack.append(num1 + num2)
                case "-":
                    stack.append(num1 - num2)
                case "*":
                    stack.append(num1 * num2)
                case "/":
                    stack.append(num1 / num2)

    return stack.pop()


print(f'{expr} = {infix_eval(expr)} (hint: {eval(expr)})')
