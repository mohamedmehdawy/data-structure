import inspect
from packages.doubleLinkedList import DoubleLinkedList

class Deque:
    # init properties
    def __init__(self, size) -> None:
        self.size = size
        self.added_elements = 0
        self.double_linked_list = DoubleLinkedList()
    
    
    @property
    def front(self):
        return self.double_linked_list.head.data
    
    @property
    def rear(self):
        return self.double_linked_list.tail.data
    
    # methods
    def is_full(self):
        """
            this functoin return the boolean value of the deque if full or not
            returns:
                the deque is full or not
        """
        return self.added_elements == self.size
    
    def check_full(self, func):
        """
            this decorator handle check full of added functions
        """
        def wrapper():
            # check if deque is full return no thing, else call the function
            if self.is_full():
                print(f"cant add the deque is full")
                return
            func()
            
            # increase added elements
            self.added_elements += 1
        
        return wrapper
    def is_empty(self):
        """
            this functoin return the boolean value of the deque if empty or not
            returns:
                the deque is empty or not
        """
        return self.added_elements == 0
    
    @check_full
    def enque_front(self, value):
        """
            this function add the value in front of deque
            parameters:
                value: the value will added in the front of deque
            returns: None
        """
        self.double_linked_list.insert_front(value)
        
def test1(data, size,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enque_front")
    
    deque = Deque(size)
    
    for ele in data:
        deque.enque_front(ele)
        
    result = str(deque)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"