class Queue:
    def __init__(self, size) -> None:
        # init proerties
        self.front = self.rear = 0
        self.added_elements = 0

        self.size = size
        self.array = [None] * size

    def _next(self, pos):
        """
            this function return the next position of the current position
            parameters:
                pos: the position will get the next of it
            returns:
                the next position of the current position 
        """
        # increase the position
        pos += 1

        # check if we in the last elements
        if pos == self.size:
            return 0
        # else, return the current position
        return pos

    def enque(self, value):
        """
            this function append the value to the queue
            parameters:
                value: the value will added to the queue
            returns: None
        """
        # check if the queue is not full
        if self.isFull():
            print("the queue is full, cant added new one")
            return
        
        # set the value in the current rear
        self.array[self.rear] = value
        
        # move the rear
        self.rear = self._next(self.rear)
        
        # increase added elements
        self.added_elements += 1
        

    def isFull(self):
        """
            this function check if the queue is full or not
            returns:
                the boolean value for the queue is full
        """
        if self.added_elements == self.size:
            return True

        return False


