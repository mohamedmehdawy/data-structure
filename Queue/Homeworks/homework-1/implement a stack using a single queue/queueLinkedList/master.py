import inspect
from .linkedList import LinkedList

class Queue:
    def __init__(self) -> None:
        # init proerties
        self.queue_list = LinkedList()

    def enque(self, value):
        """
            this function append the value to the queue
            parameters:
                value: the value will added to the queue
            returns: None
        """
        self.queue_list.insert_end(value)
        

    def deque(self):
        """
            this function remove the front of the queue
            returns: None
        """
        # check if empty, cant remove the front
        if self.isEmpty():
            print("the queue is empty, not elements to remove")
            return
        
        return self.queue_list.delete_front()
        

    def isEmpty(self):
        """
            this function check if the queue is empty or not
            returns:
                the boolean value for the queue is empty
        """
        return len(self.queue_list) == 0
    
    def front(self):
        """
            this function return the first element in the queue
        """
        # check if empty, cant remove the front
        if self.isEmpty():
            print("the queue is empty, not elements to return")
            return ""
        
        return self.queue_list.head.data
    def __len__(self):
        return len(self.queue_list)
    
    def __repr__(self) -> str:
        return str(self.queue_list)
    
    
def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enque")
    
    queue = Queue()
    
    for ele in data:
        queue.enque(ele)

    
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  


def test2(data, deque_count,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => deque")
    
    queue = Queue()
    
    for ele in data:
        queue.enque(ele)

    # deque counter
    for _ in range(deque_count):
        queue.deque()
        
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  
if __name__ == "__main__":
    
    # test 1 enque
    test1([1,2,3,4,5], "[1,2,3,4,5]")
    test1([1,2,3,4,5,6], "[1,2,3,4,5,6]")
    
    # test 2 deque
    test2([1,2,3,4,5], 1,"[2,3,4,5]")
    test2([1,2,3,4,5,6], 1,"[2,3,4,5,6]")
    test2([1,2,3,4,5,6], 7,"[]")
    test2([1,2,3,4,5,6], 7,"[]")

    # all tests passed
    print("all tests passed")