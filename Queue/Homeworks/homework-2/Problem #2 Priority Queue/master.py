import inspect
from packages.master import Queue


class PriorityQueue:
    def __init__(self) -> None:
        self.priorities = [3,2,1]
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
    def __repr__(self) -> str:
        
        
        for priority in self.priorities:
            print(f"Priority #{priority} tasks {self.queues[str(priority)]}")
        
        return ""


def test1(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"{fun_name} => enqueue")
    
    queue = PriorityQueue()
    
    for ele in data:
        queue.enqueue(ele[0], ele[1])

    
    result = str(queue)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} in {fun_name}"  

if __name__ == "__main__":
    # test 1 => enqueue
    test1([(1131, 1), (3111, 3), (2211, 2), (3161, 3)], "")
    
    # all tests passed
    print("all tests passed")