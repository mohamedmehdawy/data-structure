import inspect


class Stack:
    
    def __init__(self) -> None:
        self.array = []
    
    def push(self, value):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function push the value to the stack
        """
        self.array.append(value)
    
    def pop(self):
        """
            this function remove the last item from the array
        """
        if len(self.array):
            return self.array.pop()

        return None
    def peek(self):
        pass
    
    def isEmpty(self):
        pass
    
    def isFull(self):
        pass
    
    def clearContent(self):
        pass
    
    def __repr__(self) -> str:
        
        # convert each element in array to string to convert the array to a one string
        return ", ".join(str(item) for item in self.array)
        

def test1(data, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => push")
    
    # stack
    stk = Stack()
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # result
    result = str(stk)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    
    
def test2(data, pop_count,expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => pop")
    
    # stack
    stk = Stack()
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # pop the last element
    for _ in range(pop_count):
        stk.pop()
        
    # result
    result = str(stk)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    
if __name__ == "__main__":
    # test 1 => push
    test1([], "")
    test1([1], "1")
    test1([1,2,3,4,5], "1, 2, 3, 4, 5")
    
    # test 2 => pop
    test2([], 1, "")
    test2([1], 1, "")
    test2([1,2,3,4,5], 1, "1, 2, 3, 4")
    test2([1,2,3,4,5], 2, "1, 2, 3")

    print("all tests passed")