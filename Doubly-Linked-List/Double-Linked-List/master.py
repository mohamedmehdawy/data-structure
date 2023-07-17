class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self) -> str:
        return f'{self.data}'
    
    
    

class LinkedList:
    def __init__(self, init_values = None) -> None:
        # init pointers
        self.head = None
        self.tail = None
        self.length = 0
        
        # debug data
        self.debug_data = []
        
        # check init values
        if init_values:
            for ele in init_values:
                # should here inster end of node
                pass
    def _add_node(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function add node to debug data and increase length
            parameters:
                node: will be added to debug data
        """
        self.debug_data.append(node)
        self.length += 1
    @staticmethod
    def _link(first, second):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function make next of first link to second and prev of second link with first
            
            parameters:
                first: first node will link with second node
                second: second node will link with first node
                
        """
        if first:
            first.next = second
        
        if second:
            second.prev = first
            
    def insert_end(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function inster node to the end of linked list
            parameters:
                node: the node will inster to the end of linked list
        """
        # if linked list not have any nodes
        if self.length == 0:
            self.head = self.tail = node
        else:
            self._link(self.tail, node)
            self.tail = node
            self._add_node(node)