import inspect
from queueLinkedList.master import Queue
class Stack:
    def __init__(self) -> None:
        self.queue = Queue()
        
        
    def push(self, value): # O(n)
        """
            this function the element to the stack
            parameters:
                value: the value will added to the stack
            returns: None
        """
        # add the new element to the end
        self.queue.enqueue(value)

        # reverse the qeueu to simulate the stack
        for _ in range(len(self.queue) - 1):
            self.queue.enqueue(self.queue.dequeue())
    def peek(self):
        """
            this function remove the top element in the stack
            returns: removed element
        """
        return self.queue.front()

    def pop(self): # o(1)
        """
            this function remove the top of the stack
            returns: the deleted element
        """
        return self.queue.dequeue()
    def __repr__(self) -> str:
        return str(self.queue)
    
def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => push")
    
    stack = Stack()
    
    for ele in data:
        stack.push(ele)

    
    result = str(stack)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

def test2(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => peek")
    
    stack = Stack()
    
    # add elements
    for ele in data:
        stack.push(ele)

    
    result = str(stack.peek())
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

def test3(data, counter, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => pop")
    
    stack = Stack()
    
    # add elements
    for ele in data:
        stack.push(ele)

    # pop insted of number of counter
    for _ in range(counter):
        stack.pop()
    result = str(stack)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

if __name__ == "__main__":
    # test 1 => push
    test1([1,2,3], "[3,2,1]")
    test1([1], "[1]")
    test1([1,2], "[2,1]")
    test1([], "[]")
    
    # test 2 => peek
    test2([1,2,3], "3")
    test2([1,2], "2")
    test2([], "")
    
    # test 3 => pop
    test3([1,2,3], 0,"[3,2,1]")
    test3([1,2,3], 1,"[2,1]")
    test3([1,2,3], 2,"[1]")
    test3([1,2,3], 3,"[]")
    test3([1,2,3], 5,"[]")
    
    # all tests passed
    print("all tests passed")
