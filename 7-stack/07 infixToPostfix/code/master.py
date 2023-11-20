def infix_to_postfix(infix):
    """
        this function convert infix to postfix using Shunting-yard algorithm
        parameters:
            infix: the infix expression
        returns:
            postfix after conversion
    """
    # set order for each operator
    operators_order = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    
    # create postfix list and operators stack
    postfix_list = [None] * len(infix)
    operators_stack = []
    
    for token in infix:
        # if not operator append to postfix list
        if token not in operators_order:
            postfix_list.append(token)
        else:
            # if stack is empty or the current token is more than the last element in stack, append operator
            if not operators_stack or operators_order[operators_stack[-1]] > operators_order[token]:
                operators_stack.append(token)
            else:
                # pop operators from stack and append to list until the condition return false
                while not(operators_order[operators_stack[-1]] > operators_order[token]):
                    postfix_list.append(operators_stack.pop())
                else:
                    operators_stack.append(token)
    # check if we have operators in stack
    if operators_stack:
        for _ in operators_stack:
            postfix_list.append(operators_stack.pop())
    
    # convert list to string and return the value
    return "".join(postfix_list)

    