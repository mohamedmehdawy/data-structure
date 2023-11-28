import inspect


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
            return first_number ** second_number
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
            eval_stack.append(token)
        else:
            try:
                # get last 2 elements and pop from the stack, and do the current operation in it
                right_number = int(eval_stack.pop())
                left_number = int(eval_stack.pop())
            except:
                return "invalid postfix"


            
            # get the result
            result = handle_operator(token, left_number, right_number)
            
            # append the result after evalaution
            eval_stack.append(result)
    
    # the result will be the last and its the only element in the eval stack
    result = eval_stack.pop()
    
    return result
    
def test1(postfix, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> evalaute_postfix")
    
    result = evalaute_postfix(postfix)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    
if __name__ == "__main__":
    # test 1 => evalaute_postfix
    test1("52/", 2.5)
    test1("12+3+", 6)
    test1("123*+", 7)
    test1("23*4+", 10)
    test1("135*+72/-", 12.5)
    test1("432^^", 262144)
    test1("12+3+/", "invalid postfix")

    # all tests passed
    print("all tests passed")