def evalaute_postfix(postfix):
    """
        this function evalaute postfix and return the value
        parameters:
            postfix: the postfix value will converted
        returns:
            postfix value after evalaute
    """
    def handle_operator(operator, first_number, second_number):
        """
            this function handle operator using if and return the result
            parameters:
                operator: the operator will do in the numbers
                first_number: the first number
                second_number: the second number
            returns:
                the value after evalaution
        """
        if operator == "^":
            return first_number ^ second_number
        elif operator == "*":
            return first_number * second_number
        elif operator == "/":
            return first_number / second_number
        elif operator == "+":
            return first_number + second_number
        elif operator == "-":
            return first_number - second_number
        
    # check if less than 3 element, return the postfix
    if len(postfix) < 3:
        return postfix
    
    # operators
    operators = ["^", "*", "/", "+", "-"]
    
    # eval_stack
    eval_stack = []
    
    for token in postfix:
        # if token not operator just append to eval stack
        if not token in operators:
            eval_stack.append()
        else:
            # get last 2 elements and pop from the stack, and do the current operation in it
            left_number = int(eval_stack.pop())
            right_number = int(eval_stack.pop())
            
            # get the result
            result = handle_operator(token, left_number, right_number)
            
            # append the result after evalaution
            eval_stack.append(result)
    print(eval_stack)