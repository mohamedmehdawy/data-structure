def infixToPostfix(infix):
    # Assume: no spaces, single digits, only + - * /
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    infix += '-'		    # Whatever lowest priority: force stack got empty
    operators.append('#')   # Remove IsEmpty

    for char in infix:
        if char.isdigit():
            postfix += char
        else:
            while precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)	# higher than any in the stack

    return postfix


if __name__ == '__main__':
    assert (infixToPostfix('1+2+3') == '12+3+')
    assert (infixToPostfix('1+2*3') == '123*+')
    assert (infixToPostfix('2*3+4') == '23*4+')
    assert (infixToPostfix('1+3*5-8/2') == '135*+82/-')
    assert (infixToPostfix('2+3*4-5*6+7') == '234*+56*-7+')
