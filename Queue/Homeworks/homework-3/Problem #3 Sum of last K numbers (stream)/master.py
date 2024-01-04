class LastKNumerSumStream:
    def __init__(self, k) -> None:
        self.k = k
        self.removed = self.last_sum = 0

    def next(self, new_num):
        """
            this function take the new number and calacute the sum of streaming
            parameters:
                new_num: the new number will take the sum of it insted of k
            returns:
                the calacution after sum
        """
        # if new number is greater than k, increase removed by 1
        if new_num > self.k:
            self.removed += 1

        # set last sum
        self.last_sum = self.last_sum + new_num - self.removed

        return self.last_sum
