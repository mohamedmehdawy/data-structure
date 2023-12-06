import inspect


def infix_to_prefix(infix):
    """
        this function convert the infix to prefix
        parameters:
            infix: the infix expression
        returns:
            prefix after conversion
    """
    def reversedPostfix(infix):
        def precedence(operator):
            """
                this function return the precedence of the operator
                parameters:
                    operator: the operator will get precedence of it
                returns:
                    the precedence of the operator
            """
            if operator == "+" or operator == "-":
                return 1
            elif operator == "*" or operator == "/":
                return 2
            elif operator == "^":
                return 3
            
            return 0
    
        
        # create prefix and operator stack
        postfix_stack = []
        operators_stack = []
        
        for token in infix:
            # check if the token not a operator, append to prefix stack
            if token.isdigit() or token.islower() or token.isupper():
                postfix_stack.append(token)
            elif token == ")":
                # remove operator until arraive to (
                while operators_stack[-1] != '(':
                    postfix_stack.append(operators_stack.pop())
                    
                # pop the (
                postfix_stack.pop()
            else:
                # pop the operator stack unit the the condition return false
                while token != '(' and operators_stack and (precedence(token) < precedence(operators_stack[-1]) or (operators_stack[-1] == token and token == '^')):
                    postfix_stack.append(operators_stack.pop())
                    
                # append the current operator to the operator stack
                operators_stack.append(token)
        # if found operators append to the postfix
        while operators_stack:
            postfix_stack.append(operators_stack.pop())

        return "".join(postfix_stack)
    
    # reverse the infix
    reversed_infix = infix[::-1].replace('(', '$').replace(')', '(').replace('$', ')')
    print(reversed_infix)
    reversed_postfix = reversedPostfix(reversed_infix)
    
    return reversed_postfix[::-1]
def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => infix to prefix")
    
    result = infix_to_prefix(data)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    
    
if __name__ == "__main__":
    # infix to prefix
    test1("1+2", "+12")
    test1("9-2+3", "+-923")
    test1("4^3^2", "^4^32")
    test1("1+2+3", "++123")
    test1("1+2*3", "+1*23")
    test1("2*3+4", "+*234")
    test1("a+B-c", "-+aBc")
    test1("1+3*5-8/2", "-+1*35/82")
    test1('2+(3*(4-5)*(9/3+6))', '+2**3-45+/936')
    test1('5+4^3^2-9', '-+5^4^329')
    test1('a+B-c', '-+aBc')
    test1('a+(c^d-e)^(f+g*h)-i', '-+a^-^cde+f*ghi')
    test1('1+2^3^4-6', '-+1^2^346')
    test1('(1+2)^3^(4-6)^2+1', '+^+12^3^-4621')
    test1('2^3^4^5^6', '^2^3^4^56')
    
    # all tests passed
    print("all tests passed")