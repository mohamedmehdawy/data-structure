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

def f_stk_class_style(n):
    if n <= 1:
        return 5
    
    class RecursiveCall:
        def __init__(self,n, result = 0, is_completed=False) -> None:
            self.n = n
            self.result = result
            self.is_completed = is_completed
            
    stack = [RecursiveCall(n)]
    
    while stack:
        # get last call data
        last_call = stack[-1]
        n, result, is_completed = last_call.n, last_call.result, last_call.is_completed
        
        if not is_completed:
            
            # check last call
            if n <= 1:
                stack.append(RecursiveCall(n, 5, True))
            elif n % 3 == 0:
                stack.append(RecursiveCall(n-1-n%3, 6))
            else:
                stack.append(RecursiveCall(n-1-n%2, 8))
        else:
            stack.pop()
            
            if not stack:
                return result
            
            stack[-1].result += result
            stack[-1].is_completed = True
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
        
def test2(n):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> simulate stack class style")
    
    try:
        f_stk_result = f_stk_class_style(n)
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
    
    # test 2
    test2(10)
    test2(500)
    test2(100000)

    
    
    # all tests passed
    print("all tests passed")