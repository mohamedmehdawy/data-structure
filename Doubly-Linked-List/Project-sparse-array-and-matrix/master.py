# the node
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
            this function set value inside the list insted of the index
            parameters:
                idx: the index you will add node in it
                value: the value of the node
        """
        # check idx range
        if idx < 0 or idx > self.length:
            print(f"the index: {idx}, is out of range: {self.length}")
            return
        
        
        # set current to get idx
        current = self.head
        
        # get the valid position
        while current and current.idx < idx:
            current = current.next
        
        # create new node
        node = Node(idx, value)
        
        # check if we are in the first node
        if current == self.head or self.head is None:
            self.insert_front(node)
        
        # check if the new node will be the new tail
        elif current is None and self.acutal_length < self.length:
            self.insert_end(node)
        
        
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
                
                assert counter <= self.length
            
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
                assert counter <= self.length

            
            assert counter == self.acutal_length
            assert self.acutal_length <= self.length