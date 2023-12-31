import inspect


class Queue:
    def __init__(self, size) -> None:
        # init proerties
        self.front = self.rear = 0

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

    def deque(self):
        """
            this function remove the front of the queue
            returns: None
        """
        # check if empty, cant remove the front
        if self.isEmpty():
            print("the queue is empty, not elements to remove")
            return

        # set the current front = None
        self.array[self.front] = None

        # move the front
        self.front = self._next(self.front)

    def isFull(self):
        """
            this function check if the queue is full or not
            returns:
                the boolean value for the queue is full
        """
        return self.front == self.rear and self.array[self.front] != None

    def isEmpty(self):
        """
            this function check if the queue is empty or not
            returns:
                the boolean value for the queue is empty
        """
        return self.front == self.rear and self.array[self.front] == None

    def __repr__(self) -> str:
        # check if empty, return empty list
        if self.isEmpty():
            return "[]"

        # init result and current
        result = []
        current = self.front
        counter = None
        # loop in all array if full
        if self.isFull():
            counter = len(self.array)
        # if in normal case, rear is greater than front, just set counter =self.rear - self.front
        elif self.rear > self.front:
            counter = self.rear - self.front
        # set counter after remove and different from rear and front from the array
        else:
            counter = len(self.array) - (self.front - self.rear)
        for _ in range(counter):

            result.append(self.array[current])
            current = self._next(current)

        return str(result)


def test1(data, size, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => enque")

    queue = Queue(size)

    for ele in data:
        queue.enque(ele)

    result = str(queue)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


def test2(data, size, deque_count, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => deque")

    queue = Queue(size)

    for ele in data:
        queue.enque(ele)

    # deque counter
    for _ in range(deque_count):
        queue.deque()

    result = str(queue)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


if __name__ == "__main__":

    # test 1 enque
    test1([1, 2, 3, 4, 5], 5, "[1, 2, 3, 4, 5]")
    test1([1, 2, 3, 4, 5, 6], 5, "[1, 2, 3, 4, 5]")

    # test 2 deque
    test2([1, 2, 3, 4, 5], 5, 1, "[2, 3, 4, 5]")
    test2([1, 2, 3, 4, 5, 6], 7, 1, "[2, 3, 4, 5, 6]")
    test2([1, 2, 3, 4, 5, 6], 7, 7, "[]")
    test2([1, 2, 3, 4, 5, 6], 7, 8, "[]")

    # all tests passed
    print("all tests passed")
