import inspect
from packages.linkedList import LinkedList

class Queue:
    def __init__(self) -> None:
        # init proerties
        self.queue_list = LinkedList()

    def enqueue(self, value):
        """
            this function append the value to the queue
            parameters:
                value: the value will added to the queue
            returns: None
        """
        self.queue_list.insert_end(value)
        

    def dequeue(self):
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
    
    print(f"{fun_name} => enqueue")
    
    queue = Queue()
    
    for ele in data:
        queue.enqueue(ele)

    
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  


def test2(data, dequeue_count,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => dequeue")
    
    queue = Queue()
    
    for ele in data:
        queue.enqueue(ele)

    # dequeue counter
    for _ in range(dequeue_count):
        queue.dequeue()
        
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  
if __name__ == "__main__":
    
    # test 1 enqueue
    test1([1,2,3,4,5], "[1,2,3,4,5]")
    test1([1,2,3,4,5,6], "[1,2,3,4,5,6]")
    
    # test 2 dequeue
    test2([1,2,3,4,5], 1,"[2,3,4,5]")
    test2([1,2,3,4,5,6], 1,"[2,3,4,5,6]")
    test2([1,2,3,4,5,6], 7,"[]")
    test2([1,2,3,4,5,6], 7,"[]")

    # all tests passed
    print("all tests passed")