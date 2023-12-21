from packages.stack import Stack

class Queue:
    def __init__(self) -> None:
        self.stk1 = Stack()
        self.stk2 = Stack()
    
    @staticmethod
    def _move(first, second):
        """
            this method move elements from first element to second elemnt
            parameters:
                first: the base stack have elements
                second: the stack will elements converts to it
            retruns:
                None
        """
        while not first.isEmpty():
            second.push(first)
            
    def push(self, value):
        """
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
        
        
    