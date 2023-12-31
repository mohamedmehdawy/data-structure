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
            Time Complexity: O(1)
            Memory Complexity: O(1)
            ########################
            this function push the value to the qeueu
            parameters:
                value: the value will passed to the queue
        """
        self.stk1.push(value)

    def dequeue(self):
        """
            Time Complexity: O(n)
            Memory Complexity: O(1)
            ########################
            this function remove the first element of the queue
            retruns:
                the removed element
        """
        # if not elements to remove in stk2 move all elements from skt1

        if self.stk2.isEmpty():
            self._move(self.stk1, self.stk2)

        # remove value
        value = self.stk2.pop()

        return value

    def is_empty(self):
        """
            this function return the boolean value of stk1 is empty or not
            returns:
                status of empty of queue
        """

        return self.stk1.isEmpty() and self.stk2.isEmpty()

    def __repr__(self) -> str:

        result_stk2 = str(self.stk2)
        result_stk1 = ", ".join(reversed(str(self.stk1).split(', ')))

        result = result_stk2 + \
            f"{', ' if not self.stk2.isEmpty() and not self.stk1.isEmpty() else ''}" + \
            result_stk1

        return result


def test1(data, expected):
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


def test3(data, expected):
    func_name = inspect.currentframe().f_code.co_name

    print(f"testing => is empty")

    # queue
    queue = Queue()

    # push data
    for ele in data:
        queue.enqueue(ele)

    # result
    result = queue.is_empty()

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"


def test4(first_push, second_push, counter, expected):
    func_name = inspect.currentframe().f_code.co_name
    print(f"testing => custom test")

    # queue
    queue = Queue()

    # push data
    for ele in first_push:
        queue.enqueue(ele)

    # dequeue elements insted of counter number
    for _ in range(counter):
        queue.dequeue()

    # push data
    for ele in second_push:
        queue.enqueue(ele)

    # result
    result = str(queue)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"


if __name__ == "__main__":
    # test 1 => enqueue
    test1([], "")
    test1([1], "1")
    test1([1, 2], "1, 2")
    test1([1, 2, 3, 4, 5], "1, 2, 3, 4, 5")

    # test 2 => dequeue
    test2([], 0, "")
    test2([1], 0, "1")
    test2([1], 1, "")
    test2([1], 10, "")
    test2([1, 2, 3, 4, 5], 2, "3, 4, 5")

    # test 3 => is empty
    test3([], True)
    test3([1], False)
    test3([1, 2], False)
    test3([1, 2, 3, 4, 5], False)

    # test 4 => custom push
    test4([1, 2, 3], [4, 5, 6], 2, "3, 4, 5, 6")
    # all tests passed
    print("all tests passed")
