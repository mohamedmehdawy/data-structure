

def InfixToPostfix(infix):
    # Assume: no spaces, single digits, only + - * /
    operators = []
    postfix = ''

    def precedence(op):
        if op == '+' or op == '-':
            return 1
        return 2	# For * /

    for char in infix:
        if char.isdigit():
            postfix += char
        else:
            while operators and precedence(operators[-1]) >= precedence(char):
                postfix += operators[-1]
                operators.pop()
            operators.append(char)	# higher than any in the stack

    postfix += ''.join(reversed(operators))	# # remaining
    return postfix


if __name__ == '__main__':
    print(InfixToPostfix('1+2+3'))	# 12+3+
    print(InfixToPostfix('1+2*3'))  # 123*+
    print(InfixToPostfix('2*3+4'))  # 23*4+
    print(InfixToPostfix('1+3*5-8/2'))  # 135*+82/-
    print(InfixToPostfix('2+3*4-5*6+7'))  # 234*+56*-7+

