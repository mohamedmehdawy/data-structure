import inspect


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

    def enqueue(self, value):
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

    def dequeue(self):
        """
            this function remove the front of the queue
            returns: None
        """
        # check if empty, cant remove the front
        if self.isEmpty():
            print("the queue is empty, not elements to remove")
            return
        removed_element = self.array[self.front]
        # set the current front = None
        self.array[self.front] = None

        # move the front
        self.front = self._next(self.front)

        # deccrease added elements
        self.added_elements -= 1

        return removed_element

    def isFull(self):
        """
            this function check if the queue is full or not
            returns:
                the boolean value for the queue is full
        """
        return self.added_elements == self.size

    def isEmpty(self):
        """
            this function check if the queue is empty or not
            returns:
                the boolean value for the queue is empty
        """
        return self.added_elements == 0

    def __iter__(self):
        self.current = self.front
        self.counter = 0
        return self

    def __next__(self):
        if self.counter != self.added_elements:
            current_value = self.array[self.current]
            self.current = self._next(self.current)
            self.counter += 1
            return current_value

        raise StopIteration

    def __repr__(self) -> str:
        if self.added_elements:
            # init result and current
            result = []
            current = self.front
            for _ in range(self.added_elements):
                result.append(self.array[current])
                current = self._next(current)

            return str(result)

        return str([])


def test1(data, size, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => enque")

    queue = Queue(size)

    for ele in data:
        queue.enqueue(ele)

    result = str(queue)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


def test2(data, size, deque_count, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => deque")

    queue = Queue(size)

    for ele in data:
        queue.enqueue(ele)

    # deque counter
    for _ in range(deque_count):
        queue.dequeue()

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

    tt = Queue(3)
    tt.enqueue(1)
    tt.enqueue(2)
    tt.enqueue(3)

    # all tests passed
    print("all tests passed")
