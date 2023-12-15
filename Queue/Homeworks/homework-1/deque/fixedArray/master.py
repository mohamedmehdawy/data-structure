import inspect
class Deque:
    # init properties
    def __init__(self, size) -> None:
        self.front = self.rear = 0
        self.size = size
        self.added_elements = 0
        self.array = [None] * size

    
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
    
    def check_empty(func):
        """
            this decorator handle check empty of removing functions
        """
        def wrapper(self):
            # check if deque is empty return no thing, else call the function
            if self.is_empty():
                print(f"cant remove the element the deque is empty")
                return
            func(self)
            
            # increase added elements
            self.added_elements -= 1
        
        return wrapper
    
    @check_full
    def enque_front(self, value):
        """
            this function add the value in front of deque
            parameters:
                value: the value will added in the front of deque
            returns: None
        """
        self.front = self._prev(self.front)
        self.array[self.front] = value
    
    @check_full
    def enque_rear(self, value):
        """
            this function add the value in end of deque
            parameters:
                value: the value will added in the end of deque
            returns: None
        """
        self.array[self.rear] = value
        self.rear = self._next(self.rear)

    @check_empty
    def dequeue_front(self):
        """
            this function remove the first element in the list
            returns: removed value
        """
        deleted_value = self.array[self.front] 
        self.array[self.front] = None
        self.front = self._next(self.front)
        return deleted_value
    
    @check_empty
    def dequeue_rear(self):
        """
            this function remove the last element in the list
            returns: removed value
        """
        self.rear = self._prev(self.rear)
        deleted_value = self.array[self.rear] 
        self.array[self.rear] = None
        
        return deleted_value
    
    def __repr__(self) -> str:
        
        # set current position, and will start with front
        current = self.front
        result = []
        for _ in range(self.added_elements):
            result.append(str(self.array[current]))
            current = self._next(current)
            
        return "[" + ",".join(result) + "]"
        
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

def test2(data, size, front, rear, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enque_rear")
    
    deque = Deque(size)
    
    for ele in data:
        deque.enque_rear(ele)
        
    result = str(deque)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    assert deque.front == front, f"Mismatch between expected front={front}, and result front={deque.front} in {fun_name}"
    assert deque.rear == rear, f"Mismatch between expected rear={rear}, and result rear={deque.rear} in {fun_name}"

def test3(data, size, front, rear, count,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => deque front")
    
    deque = Deque(size)
    
    # add data
    for ele in data:
        deque.enque_rear(ele)
    
    # remove elements from front insted of count
    for _ in range(count):
        deque.dequeue_front()
        
    result = str(deque)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    assert deque.front == front, f"Mismatch between expected front={front}, and result front={deque.front} in {fun_name}"
    assert deque.rear == rear, f"Mismatch between expected rear={rear}, and result rear={deque.rear} in {fun_name}"

def test4(data, size, front, rear, count,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => deque rear")
    
    deque = Deque(size)
    
    # add data
    for ele in data:
        deque.enque_rear(ele)
    
    # remove elements from back insted of count
    for _ in range(count):
        deque.dequeue_rear()
        
    result = str(deque)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"
    assert deque.front == front, f"Mismatch between expected front={front}, and result front={deque.front} in {fun_name}"
    assert deque.rear == rear, f"Mismatch between expected rear={rear}, and result rear={deque.rear} in {fun_name}"


if __name__ == "__main__":
    
    # test 1 => enque front
    test1([1,2,3], 6, 3, 0, "[3,2,1]")
    test1([1,2,3,4,5,6], 6, 0, 0, "[6,5,4,3,2,1]")
    test1([1,2,3,4,5,6], 5, 0, 0, "[5,4,3,2,1]")

    # test 2 => enque rear
    test2([1,2,3], 6, 0, 3, "[1,2,3]")
    test2([1,2,3,4,5,6], 6, 0, 0, "[1,2,3,4,5,6]")
    
    # test 3 => deque front
    test3([1,2,3], 6, 0, 3, 0,"[1,2,3]")
    test3([1,2,3], 6, 1, 3, 1,"[2,3]")
    test3([1,2,3,4,5,6], 6, 3, 0, 3,"[4,5,6]")
    test3([1,2,3,4,5,6], 6, 0, 0, 6,"[]")

    # test 4 => deque back
    test4([1,2,3], 6, 0, 3, 0,"[1,2,3]")
    test4([1,2,3], 6, 0, 2, 1,"[1,2]")
    test4([1,2,3,4,5,6], 6, 0, 3, 3,"[1,2,3]")
    test4([1,2,3,4,5,6], 6, 0, 0, 6,"[]")
    test4([1,2,3,4,5,6], 6, 0, 0, 10,"[]")

    # all tests passed
    print("all tests passed")