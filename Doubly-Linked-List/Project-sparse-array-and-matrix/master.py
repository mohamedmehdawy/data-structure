# the node
class Node:
    def __init__(self, idx, value) -> None:
        """
            the init of node object
            parameters:
                idx: the index
                the value of node
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
        
    def debug_verify_data_integrity(self):
        """
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
            assert self.length == len(self.debug_data)
            
            # check forward
            # check elements length and the sorted if them
            current = self.head.next
            counter = 0
            
            while current:
                # the idx should be sorted
                assert  current.prev.idx < current.idx
                counter += 1
                current = current.next
                
            
            assert counter == self.acutal_length
            assert self.acutal_length <= self.length
            
            # check backword
            # check elements length and the sorted if them
            current = self.tail.prev
            counter = 0
            
            while current:
                # the idx should be sorted
                assert current.idx.next > current.idx
                counter += 1
                current = current.prev
            
            assert counter == self.acutal_length
            assert self.acutal_length <= self.length