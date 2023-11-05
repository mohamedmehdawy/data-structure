import inspect


class Stack:
    
    def __init__(self) -> None:
        self.array = []
    
    def push(self, value):
        """
            this function push the value to the stack
        """
        self.array.append(value)
    
    def pop(self):
        pass
    
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
    
    
if __name__ == "__main__":
    test1([], "")
    test1([1], "1")
    
    print("all tests passed")