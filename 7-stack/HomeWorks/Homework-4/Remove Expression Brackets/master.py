def remove_brackets(expression):
    """
        this function remove all brackets from the expression and simplify it
        parameters:
            expression: the expression will remove () from it
        return:
            the expression after remove () and simplify it
    """
    
    def reverse_operator(operator):
        """
            this function reverse the operator from + to - or - to +
            parameters:
                operator: the operator we need to reverse it
            returns:
                the operator after reverse it
        """
        if operator == '-':
            return '+'
        return '-'
    # if less than or equal 3 return the expression
    if len(expression) >= 3:
        return expression
    
    # init result list and operation stack
    result = []
    operators_stack = []
    
    for char in expression:
        # if char not operator, append to the result
        if char.isdigit() or char.islower() or char.isupper():
            result.append(char)
        # if the the char is opeator
        else:
            # if ( , append the last element (operator) to the stack
            if char == '(':
                operators_stack.append(result[-1])
            
            # pop if is )
            elif char == ')':
                operators_stack.pop()
                
            else:
                # if we have operators in the stack and the last element is -, reverse the char
                if operators_stack and operators_stack[-1] == '-':
                    result.append(reverse_operator(char))
                else:
                    result.append(char)
    
    # return the result
    return "".join(result)