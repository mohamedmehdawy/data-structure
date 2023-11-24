

def InfixToPostfix(infix):
    # Assume: no spaces, single digits, only + - * /
    operators = []
    postfix = ''
    
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0            # ( is 0
    
    infix += '-'		    # Whatever lowest priority: force stack got empty
    operators.append('#')   # Remove IsEmpty

    for char in infix:
        if char.isdigit():
            postfix += char
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                postfix += operators[-1]
                operators.pop()
            operators.pop() # pop (
        else:
            while precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)	# higher than any in the stack
    return postfix


if __name__ == '__main__':
    assert (InfixToPostfix('1+2+3') == '12+3+')
    assert (InfixToPostfix('1+2*3') == '123*+')
    assert (InfixToPostfix('2*3+4') == '23*4+')
    assert (InfixToPostfix('1+3*5-8/2') == '135*+82/-')
    assert (InfixToPostfix('2+3*4-5*6+7') == '234*+56*-7+')

    assert (InfixToPostfix('2+(3*4)') == '234*+')
    assert (InfixToPostfix('2+(3*(4-5*2)*(9/3+6))') == '23452*-*93/6+*+')
