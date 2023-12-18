import inspect
from queueLinkedList.master import Queue
class Stack:
    def __init__(self) -> None:
        self.queue = Queue()
        
        
    def push(self, value):
        """
            this function the element to the stack
            parameters:
                value: the value will added to the stack
            returns: None
        """
        self.queue.enque(value)
    
    def peek(self):
        """
            this function remove the top element in the stack
            returns: removed element
        """
        return self.queue.queue_list.delete_back()
    def __repr__(self) -> str:
        result = []
        
        for index in range(len(self.queue.queue_list) - 1, -1, -1):
            result.append(str(self.queue.queue_list.get_nth(index + 1).data))
        
        return "[" + ", ".join(result) + "]"
    
def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => push")
    
    stack = Stack()
    
    for ele in data:
        stack.push(ele)

    
    result = str(stack)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

def test2(data, counter, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => peek")
    
    stack = Stack()
    
    # add elements
    for ele in data:
        stack.push(ele)

    # remove insted of counter
    for _ in range(counter):
        stack.peek()
    
    result = str(stack)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

if __name__ == "__main__":
    # test 1 => push
    test1([1,2,3], "[3, 2, 1]")
    test1([1], "[1]")
    test1([1,2], "[2, 1]")
    test1([], "[]")
    
    # test 2 => peek
    test2([1,2,3], 0,"[3, 2, 1]")
    test2([1,2,3], 1,"[2, 1]")
    test2([1,2,3], 4,"[]")

    # all tests passed
    print("all tests passed")
