import inspect
from packages.doubleLinkedList import DoubleLinkedList
class Deque:
    # init properties
    def __init__(self, size) -> None:
        self.front = self.rear = 0
        self.size = size
        self.added_elements = 0
        self.double_linked_list = DoubleLinkedList()

    
    # methods
    def _next(self, pos):
        """
            this function return the next of position
        """
        pos += 1
        if pos == self.size:
            return 0
        return pos
    
    def _prev(self, pos):
        """
            this function return the prev of position
        """
        pos -= 1
        if pos == -1:
            return self.size - 1
        return pos
    def is_full(self):
        """
            this functoin return the boolean value of the deque if full or not
            returns:
                the deque is full or not
        """
        return self.added_elements == self.size
    
    def check_full(func):
        """
            this decorator handle check full of added functions
        """
        def wrapper(self, value):
            # check if deque is full return no thing, else call the function
            if self.is_full():
                print(f"cant add the deque is full")
                return
            func(self, value)
            
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
        self.front = self._prev(self.front)
    def __repr__(self) -> str:
        return str(self.double_linked_list)
def test1(data, size, front, rear, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enque_front")
    
    deque = Deque(size)
    
    for ele in data:
        deque.enque_front(ele)
        
    result = str(deque)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    assert deque.front == front, f"Mismatch between expected front={front}, and result front={deque.front} in {fun_name}"
    assert deque.rear == rear, f"Mismatch between expected rear={rear}, and result rear={deque.rear} in {fun_name}"


if __name__ == "__main__":
    
    # test 1 => enque front
    test1([1,2,3], 6, 3, 0, "[3,2,1]")
    
    # all tests passed
    print("all tests passed")