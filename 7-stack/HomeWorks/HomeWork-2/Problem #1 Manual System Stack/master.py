import inspect


def f(n):
    if n <= 1:
        return 5
    if n % 3 == 0:
        return 6 + f(n-1-n%3)
    return 8 + f(n-1-n%2)

def f_stk(n):
    """
        this function simulate stack of recursion for function f
        parameters:
            n: the number
        returns:
            the result after end simulate for recursion
    """
    # init stack
    stack = []
    
    while n > 1:
        if n % 3 == 0:
            stack.append(6)
            n = n - 1 - n % 3
        else:
            stack.append(8)
            n = n - 1 - n % 2
    # init result
    result = 5
    
    # make stack empty
    while stack:
        result += stack[-1]
        stack.pop()
        
    return result


def test1(n):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> simulate stack")
    
    try:
        f_stk_result = f_stk(n)
        f_result = f(n)
        
        print(f"f result: {f_result}, stk result: {f_stk_result}")
        assert f_result == f_stk_result
        
    except:
        print(f"stk result: {f_stk_result}")


    
if __name__ == "__main__":
    # test 1
    test1(10)
    test1(500)
    test1(100000)

    
    
    # all tests passed
    print("all tests passed")