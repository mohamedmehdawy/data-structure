import inspect


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
        num //= 10
        
    # create the stack
    stack = current_list.copy()
    stack.reverse()
    
    # check trailing zeros
    while stack[len(stack) - 1] == 0:
        stack.pop()
    # return the stack
    return "".join(str(stack[index]) for index in range(len(stack) - 1, -1, -1))

def test1(num, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => reverse_number")
    
    result = reverse_number(num)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    

if __name__ == "__main__":
    
    # test 1 => reverse_number
    test1(12345000, "54321")
    test1(5102030, "302015")
    
    # all tests passed
    print("all tests passed")