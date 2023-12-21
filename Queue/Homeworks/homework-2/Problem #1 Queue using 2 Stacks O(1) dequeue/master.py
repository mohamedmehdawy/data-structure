import inspect
from packages.stack import Stack

class Queue:
    def __init__(self) -> None:
        self.stk1 = Stack()
        self.stk2 = Stack()
    
    @staticmethod
    def _move(first, second):
        """
            Time Complexity: O(n)
            Memory Complexity: O(1)
            ########################
            this method move elements from first element to second elemnt
            parameters:
                first: the base stack have elements
                second: the stack will elements converts to it
            retruns:
                None
        """
        while not first.isEmpty():
            second.push(first.pop())
            
    def enqueue(self, value):
        
        """
            Time Complexity: O(n)
            Memory Complexity: O(1)
            ########################
            this function push the value to the qeueu
            parameters:
                value: the value will passed to the queue
        """
        if self.stk1.isEmpty():
            self.stk1.push(value)
            return
        
        # move elements from stk1, to stk2 to reverse it
        self._move(self.stk1, self.stk2)
        
        # add value to stk2
        self.stk2.push(value)
        
        # move elements from stk2, to stk1
        self._move(self.stk2, self.stk1)
        
    def dequeue(self):
        """
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function remove the first element of the queue
            retruns:
                the removed element
        """
        return self.stk1.pop()
    
    def __repr__(self) -> str:
        return str(self.stk1)
    
def test1(data,expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => enqueue")
    
    # queue
    queue = Queue()
    
    # push data
    for ele in data:
        queue.enqueue(ele)
    
    # result
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"

def test2(data, counter, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => dequeue")
    
    # queue
    queue = Queue()
    
    # push data
    for ele in data:
        queue.enqueue(ele)
    
    # dequeue elements insted of counter number
    for _ in range(counter):
        queue.dequeue()
        
    # result
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"

if __name__ == "__main__":
    # test 1 => enqueue
    test1([], "")
    test1([1], "1")
    test1([1,2], "1, 2")
    test1([1, 2, 3, 4, 5], "1, 2, 3, 4, 5")
    
    # test 2 => dequeue
    test2([], 0, "")
    test2([1], 0, "1")
    test2([1], 1, "")
    test2([1], 10, "")
    test2([1, 2, 3, 4, 5], 2, "3, 4, 5")

    # all tests passed
    print("all tests passed")