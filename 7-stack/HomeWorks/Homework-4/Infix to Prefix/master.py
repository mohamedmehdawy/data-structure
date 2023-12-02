import inspect


def infix_to_prefix(infix):
    """
        this function convert the infix to prefix
        parameters:
            infix: the infix expression
        returns:
            prefix after conversion
    """
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
    
    # reverse the infix
    infix = infix[::-1]
    
    # create prefix and operator stack
    prefix_stack = []
    operators_stack = []
    
    for token in infix:
        # check if the token not a operator, append to prefix stack
        if token.isdigit() or token.islower() or token.isupper():
            prefix_stack.append(token)
        else:
            # pop the operator stack unit the the condition return false
            while operators_stack and (precedence(token) < precedence(operators_stack[-1]) or (operators_stack[-1] == token and token == '^')):
                prefix_stack.append(operators_stack.pop())
                
            # append the current operator to the operator stack
            operators_stack.append(token)
            
    # check if we have operators, append it to the perfix stack
    while operators_stack:
        prefix_stack.append(operators_stack.pop())
    
    # reverse the prefix stack
    prefix_stack.reverse()
    
    # convert to string
    result = "".join(prefix_stack)
    
    return result

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
    
    # all tests passed
    print("all tests passed")