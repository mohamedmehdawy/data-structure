def reverse_number(num):
    """
        this function take the int number and reverse it and store in a stack
        parameters:
            num: the num will be reverse
        return:
            the num after reversed
    """
    # check if the num is unsigned
    if num <= 0:
        assert "not valid number"
        return
    
    # current list
    current_list = []
    
    # get the last number from each num and store it in current list
    
    while num > 0:
        current_number = num % 10
        current_list.append(current_number)
        num /= 10
        
    # create the stack
    stack = current_list.copy().reverse()
    
    # check trailing zeros
    while stack[len(stack) - 1] == 0:
        stack.pop()
        
    # return the stack
    return "".join(stack)

# def test1(data, expected):
    