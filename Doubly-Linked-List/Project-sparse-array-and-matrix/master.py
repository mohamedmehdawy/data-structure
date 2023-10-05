# the node
import inspect


class Node:
    def __init__(self, idx, value) -> None:
        """
            the init of node object
            parameters:
                idx: the index
                value: the value of node
        """
        # create and set index and value
        self.idx = idx
        self.value = value
        
        # create next and prev pointers and set both = none
        self.prev = self.next = None
        
    def __repr__(self) -> str:
        return f"{self.value}@{self.idx}"
    

# SparseArray
class SparseArray:
    def __init__(self, length) -> None:
        # the fixed length
        self.length = length
        
        # the actual length
        self.acutal_length = 0
        
        # create and set head and tail
        self.head = self.tail = None    
        
        # debug data
        self.debug_data = []
        
    
    def _add_node(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function add the node to debug data and increase the actual length
            parameters:
                node: the node will add to debug data
        """
        # add the node to the debug data
        self.debug_data.append(node)
        
        # increase the actual length
        self.acutal_length += 1
        
    def _link(self, first, second):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function link two node together
            parameters:
                first: the first node, the next will link with second
                second: the second node, the prev will link with first
        """
        if first:
            first.next = second
        
        if second:
            second.prev = first
    def insert_front(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function insert the node in the head
            paramerts:
                node: the node will be in the head
        """
        # check if empty
        if self.acutal_length == 0:
            self.head = self.tail = node
        else:
            # link new head with current head
            self._link(node, self.head)
            
            # set new head
            self.head = node
        # increase the actual length
        self._add_node(node)
        
        self.debug_verify_data_integrity()
    def insert_end(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function insert the node in the tail
            parameters:
                node: the node will be the new tail
        """
        if self.acutal_length == 0:
            self.insert_front(node)
        else:
            # link new head with current tail
            self._link(self.tail, node)
            
            # set new tail
            self.tail = node
        # increase the actual length
        self._add_node(node)
    def set_value(self, idx, value):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function set value inside the list insted of the index
            parameters:
                idx: the index you will add node in it
                value: the value of the node
        """
        # check idx range
        if idx < 0 or idx > self.length:
            print(f"the index: {idx}, is out of range: {self.length}")
            return
        
        # create new node
        node = Node(idx, value)
        
        # if no element insert the node or the node will be the head
        if self.acutal_length == 0:
            self.insert_front(node)

        else:
            # set current to get idx
            current = self.head
            
            # get the valid position
            while current and current.idx < idx:
                current = current.next
            
            # first check if it the tail
            if current is None:
                self.insert_end(node)
            else:
                if self.acutal_length < self.length and (current.idx != idx):
                    # check if new node will be the new head
                    if current is self.head:
                        self.insert_front(node)
                    # insert node before the current
                    else:
                        self._link(current.prev, node)
                        self._link(node, current)
                        
                        # increase actual length
                        self._add_node(node)
                
                # override current value
                elif current.idx == idx:
                    current.value = value
                else:
                    print(f"the list is full, cant add: {value}")
        
        self.debug_verify_data_integrity()
    
    def __getitem__(self, idx):
        """
            this function the node by the idx
            parameters:
                idx: the index of the list
            return:
                the node have the current idx
        """
        
        # check if the list is empty
        if self.length == 0 or idx < 0 or idx > self.length:
            return None
        
        # set current
        current = self.head
        
        while current and current.idx != idx:
            current = current.next
        
        # return the value
        return current.value if current else None
    def debug_verify_data_integrity(self):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function check the data integrity is correct or not
        """
        # if the linked list is empty
        if self.acutal_length == 0:
            assert self.head is None
            assert self.tail is None
            return
        
        # the head and tail should not be none, and the prev of head and next of tail should be none
        assert self.head is not None
        assert self.head.prev is None
        assert self.tail is not None
        assert self.tail.next is None
        
        # if we have one element
        if self.acutal_length == 1:
            assert self.head is self.tail
        elif self.acutal_length == 2:
            assert self.head.next is self.tail
        else:
            # check length and debug data length
            assert self.acutal_length == len(self.debug_data)
            
            # check forward
            # check elements length and the sorted if them
            current = self.head.next
            counter = 1
            
            while current:
                # the idx should be sorted
                assert  current.prev.idx < current.idx
                counter += 1
                current = current.next
                
                assert counter <= self.length
            
            assert counter == self.acutal_length, f"the counter is: {counter}, the acutal_length is: {self.acutal_length}"
            assert self.acutal_length <= self.length
            
            # check backword
            # check elements length and the sorted if them
            current = self.tail.prev
            counter = 1
            
            while current:
                # the idx should be sorted
                assert current.next.idx > current.idx
                counter += 1
                current = current.prev
                assert counter <= self.length

            
            assert counter == self.acutal_length
            assert self.acutal_length <= self.length
            
    
    def print_as_array(self):
        """
            this function print the list like array with empty places
        """
        
        # check if empty, return no thing
        if self.length == 0:
            return ""
        
        # set current and prev index and result
        current = self.head
        prev_idx = -1 if current.idx != 0 else 0 # if the first index found start with him else start from -1
        result_parts = []
        
        # loop until arrive to the tail
        while current:
            # add the diffrence between prev index and current index
            for _ in range(current.idx - prev_idx - 1):
                result_parts.append("0")
            
            # add the current value
            result_parts.append(str(current.value))
            
            # reset prev index and move current
            prev_idx = current.idx
            current = current.next
        
        # check if found difference between prev idx and length, if true fill empty data in result
        
        if self.length > prev_idx + 1:
            diff = self.length - prev_idx - 1 # difference between length and prev idx, so dont need to add
            for _ in range(diff):
                result_parts.append("0")
        
        # the result
        result = " ".join(result_parts)
        
        # return the result
        return result
    
    def __repr__(self) -> str:
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function print the list
        """
        result = ""
        current = self.head
        for _ in range(self.acutal_length):
            result += f"{current.value}@{current.idx}{', ' if current is not self.tail else ''}"
            current = current.next
        return result
def test1(data, length, expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => set value")
    
    ll = SparseArray(length)
    
    # set the data
    for ele in data:
        ll.set_value(ele[0], ele[1])
    
        
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {func_name}"
    
def test2(data, length, idx,expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => get value")
    
    ll = SparseArray(length)
    
    # set the data
    for ele in data:
        ll.set_value(ele[0], ele[1])
    
    result = ll[idx]
    assert str(result) == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    
def test3(data, length,expected):
    func_name = inspect.currentframe().f_code.co_name
    
    print(f"testing => print as array")
    
    ll = SparseArray(length)
    
    # set the data
    for ele in data:
        ll.set_value(ele[0], ele[1])
    
    result = ll.print_as_array()
    assert str(result) == expected, f"Mismatch between expected={expected}, and result={result} in {func_name}"
    

if __name__ == "__main__":
    # test 1 => set value
    # test1([], 15,"")
    # test1([[1,10]], 2, "10@1")
    # test1([[1,10], [2, 12]], 2,"10@1, 12@2")
    # test1([[1,10], [2, 12]], 1,"10@1")
    # test1([[1,10], [5,12], [0, 5]], 5, "5@0, 10@1, 12@5")
    test1([[5,50], [2,20], [8,80], [4,4000], [4,40]], 15, "20@2, 40@4, 50@5, 80@8")
    
    # test 2 => get value
    # test2([], 10, 0, "None")
    # test2([[0,20]], 10, 0, "20@0")
    # test2([[1,10], [5,12], [0, 5]], 5, 0,"5@0")
    # test2([[1,10], [5,12], [0, 5], [10,5]], 10, 10,"5@10")
    # test2([[1,10], [5,12], [0, 5], [10,5]], 10, 50,"None")
    # test2([[1,10], [5,12], [0, 5], [10,5]], 10, -1,"None")
    test2([[5,50], [2,20], [8,80], [4,4000], [4,40]], 15, 8, "80")
    test2([[5,50], [2,20], [8,80], [4,4000], [4,40]], 15, 9, "None")
    
    # test 3 => print as array
    test3([], 0, "")
    test3([[0,1]], 1, "1")
    test3([[0,1],[5,2],[3,4],], 6, "1 0 0 4 0 2")
    test3([[5,50], [2,20], [8,80], [4,4000], [4,40]], 15, "0 0 20 0 40 50 0 0 80 0 0 0 0 0 0")
    
    # all tests passed
    print("all tests passed")