from packages.queue import Queue


class LastKNumerSumStream:
    def __init__(self, k) -> None:
        self.k = k
        # queue stream
        self.queue_stream = Queue(k)

    def next(self, new_num):
        """
            this function take the new number and calacute the sum of streaming
            parameters:
                new_num: the new number will take the sum of it insted of k
            returns:
                result of the calacution after sum
        """
        # if the queue is full, remove the first element
        if self.queue_stream.isFull():
            self.queue_stream.deque()

        # add the new number to queue stream
        self.queue_stream.enque(new_num)

        # init result
        result = 0

        # sum the elements of the queue
        for ele in self.queue_stream:
            result += ele
        # return the result
        return result


if __name__ == "__main__":
    processor = LastKNumerSumStream(4)

    while True:
        num = int(input())

        print(f"sum of last k numbers: {processor.next(num)}")
