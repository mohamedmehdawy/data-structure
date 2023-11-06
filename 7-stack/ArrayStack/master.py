import inspect


class Stack:
    
    def __init__(self, length) -> None:
        self.array = []
        self.length = length
    def push(self, value):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function push the value to the stack
        """
        if not self.length == len(self.array):
            
            self.array.append(value)
        else:
            print(f"the stack is full, cant add: {value}")
    
    def pop(self):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function remove the last item from the array
        """
        if len(self.array):
            return self.array.pop()

        return None
    def peek(self):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function return the last element of the array
        """
        # if array is empty return none
        if not len(self.array):
            return None
        
        # return last element
        return self.array[len(self.array) - 1]
        
    
    def isEmpty(self):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function check if the array is empty or not
        """
        return not len(self.array)
    
    def isFull(self):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function check if the array is full or not
        """  
        return self.length == len(self.array)
  
    def clearContent(self):
        pass
    def __repr__(self) -> str:
        
        # convert each element in array to string to convert the array to a one string
        reversed_array = self.array.copy()
        reversed_array.reverse()
        
        return ", ".join(str(item) for item in reversed_array)
        

def test1(data, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => push")
    
    # stack
    stk = Stack(10)
    
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
    stk = Stack(10)
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # pop the last element
    for _ in range(pop_count):
        stk.pop()
        
    # result
    result = str(stk)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"

def test3(data, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => peek")
    
    # stack
    stk = Stack(10)
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # result
    result = str(stk.peek())
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"

def test4(data, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => is empty")
    
    # stack
    stk = Stack(10)
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # result
    result = stk.isEmpty()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    
def test5(data, length,expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => is full")
    
    # stack
    stk = Stack(length)
    
    # push data
    for ele in data:
        stk.push(ele)
        
    # result
    result = stk.isFull()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    
if __name__ == "__main__":
    # test 1 => push
    test1([], "")
    test1([1], "1")
    test1([1,2,3,4,5], "5, 4, 3, 2, 1")
    test1([1,2,3,4,5,6,7,8,9,10], "10, 9, 8, 7, 6, 5, 4, 3, 2, 1")
    test1([1,2,3,4,5,6,7,8,9,10,11], "10, 9, 8, 7, 6, 5, 4, 3, 2, 1")

    # test 2 => pop
    test2([], 1, "")
    test2([1], 1, "")
    test2([1,2,3,4,5], 1, "4, 3, 2, 1")
    test2([1,2,3,4,5], 2, "3, 2, 1")
    
    # test 3 => peek
    test3([], "None")
    test3([1], "1")
    test3([1,2,3,4,5], "5")
    
    # test 4 => is empty
    test4([], True)
    test4([1], False)
    test4([1,2,3,4,5], False)
    
    # test 5 => is full
    test5([], 0, True)
    test5([1,2,3], 2, True)
    test5([1,2,3], 3, True)
    test5([1,2,3,4], 5, False)



    print("all tests passed")