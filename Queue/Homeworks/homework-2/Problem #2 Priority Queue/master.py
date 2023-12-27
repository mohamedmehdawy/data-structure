import inspect
from packages.master import Queue


class PriorityQueue:
    def __init__(self) -> None:
        self.priorities = [3, 2, 1]
        self.queues = {
            '1': Queue(),
            '2': Queue(),
            '3': Queue(),
        }

    def enqueue(self, value, priority):
        """
            this function add the value to queue insted of his priority
            parameters:
                value: the value will add to the queue
                priority: the priority of the value
        """

        self.queues[str(priority)].enqueue(value)

    def dequeue(self):
        """
            this function remove the last element in queue insted of top priority has value
            returns:
                removed element if found
        """
        # loop until find highst priority queue and remove first element of it
        for priority in self.priorities:
            if len(self.queues[str(priority)]):
                return self.queues[str(priority)].dequeue()

        # if no elements in queues, return none
        return None

    def empty(self):
        """
            this funciton return the queues if empty or not
            returns: the status of the empty value
        """
        for priority in self.priorities:
            if not self.queues[str(priority)].isEmpty():
                return False
        return True

    def __repr__(self) -> str:

        for priority in self.priorities:
            print(f"Priority #{priority} tasks {self.queues[str(priority)]}")

        return ""


def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => enqueue")

    tasks = PriorityQueue()

    for ele in data:
        tasks.enqueue(ele[0], ele[1])

    result = str(tasks)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


def test2(data, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => empty")

    tasks = PriorityQueue()

    for ele in data:
        tasks.enqueue(ele[0], ele[1])

    result = tasks.empty()

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


def test3(data, counter, expected):
    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => dequeue")

    tasks = PriorityQueue()

    # add elements
    for ele in data:
        tasks.enqueue(ele[0], ele[1])

    # remove elements insted of number of counter
    for _ in range(counter):
        tasks.dequeue()

    result = str(tasks)

    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"


def test4():
    """
        simulate the tutorail test
    """

    fun_name = inspect.currentframe().f_code.co_name

    print(f"{fun_name} => simulate the tutorail test")

    tasks = PriorityQueue()

    tasks.enqueue(1131, 1)
    tasks.enqueue(3111, 3)
    tasks.enqueue(2211, 2)
    tasks.enqueue(3161, 3)

    # for print
    print(tasks)

    print(tasks.dequeue())
    print(tasks.dequeue())

    tasks.enqueue(1535, 1)
    tasks.enqueue(2815, 2)
    tasks.enqueue(3845, 3)
    tasks.enqueue(3145, 3)

    while not tasks.empty():
        print(tasks.dequeue(), end=' ')
    print()


if __name__ == "__main__":
    # test 1 => enqueue
    test1([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], "")

    # test 2 => empty
    test2([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], False)
    test2([(1131, 1), (2211, 2)], False)
    test2([(1131, 1)], False)
    test2([], True)

    # test 3 => dequeue
    test3([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], 0, "")
    test3([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], 1, "")
    test3([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], 2, "")
    test3([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], 6, "")

    # test 4 => simulate the tutorail test
    test4()

    # all tests passed
    print("all tests passed")
