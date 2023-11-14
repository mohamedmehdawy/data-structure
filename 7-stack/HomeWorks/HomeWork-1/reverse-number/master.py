import inspect
class Solution(object):
    def reverse(self, x):
        
        # check sign first
        sign = 1 if x > -1 else -1
        
        # convert number to absolute value
        x = abs(x)
        
        # current list
        stack = []
        
        # get the last number from each num and store it in current list
        
        while x > 0:
            current_number = x % 10
            stack.append(current_number)
            x //= 10
            
        # put the numbers from stack
        tens = 1
        while stack:
            x = stack[-1] * tens + x
            tens *= 10
            stack.pop()
        
        # set x with sign
        x = sign * x
        
        # check range
        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        # return the reversed number
        return  x
        


def test1(num, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => reverse_number")
    
    result = Solution().reverse(num)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    

if __name__ == "__main__":
    
    # test 1 => reverse_number
    test1(12345000, 54321)
    test1(5102030, 302015)
    test1(1534236469, 0)
    
    # all tests passed
    print("all tests passed")