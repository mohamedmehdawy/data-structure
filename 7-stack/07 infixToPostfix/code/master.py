import inspect


def infix_to_postfix(infix):
    """
        this function convert infix to postfix using Shunting-yard algorithm
        parameters:
            infix: the infix expression
        returns:
            postfix after conversion
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


        return 0
    
    # create postfix list and operators stack
    postfix_list = []
    operators_stack = []
    
    # remove empty
    operators_stack.append("#")
    
    # for make in the end operator stack empty with real operators, what ever lowest priority
    infix += '-'
    
    for token in infix:
        # if not operator append to postfix list
        if token.isdigit():
            postfix_list.append(token)
        else:
                # if the operator is ) pop last element until arraive to (
                if token == ")":
                    
                    while operators_stack[-1] != '(':
                        postfix_list.append(operators_stack.pop())
                    
                    # remove (
                    operators_stack.pop()
                else:
                    # pop operators from stack and append to list until the condition return false
                    while token != '(' and operators_stack[-1] != '(' and not(precedence(operators_stack[-1]) < precedence(token)):
                        postfix_list.append(operators_stack.pop())
                    # if stack is empty or the current token is more than the last element in stack
                    # or iteration end, append operator
                    operators_stack.append(token)
                
    # convert list to string and return the value
    return "".join(postfix_list)

def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => infix to posfix")
    
    result = infix_to_postfix(data)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    
if __name__ == "__main__":
    # test1 => infix to posfix
    test1("1+3*5-8/2", "135*+82/-")
    test1("1+2*3", "123*+")
    test1("2+3*4-5*6+7", "234*+56*-7+")
    test1("(1+2)*3", "12+3*")

    test1("2+(3*(4-5*2)*(9/3+6))", "23452*-*93/6+*+")
    
    # all tests passed
    print("all tests passed")