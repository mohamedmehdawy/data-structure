import inspect

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
                self.insert_end(ele)
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
            
    def insert_end(self, value):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function inster node to the end of linked list
            parameters:
                value: the value will add in the end of linked list as node
        """
        # the node
        node = Node(value)
        
        # if linked list not have any nodes
        if self.length == 0:
            self.head = self.tail = node
            
        else:
            self._link(self.tail, node)
            self.tail = node
        self._add_node(node)
        
        # debug verify data
        self.debug_verify_data_integrity()
    def debug_print_address(self):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function print nodes with address
        """
        cur = self.head
        
        while cur:
            print(f"{cur.data}@{id(cur)}", end="\t->\t")
            cur = cur.next
        
        print('None')
        
    def debug_print_node(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function print node with prev and next
            parameters:
                node: the target node will be print
        """
        # handel if node is none
        if node == None:
            print("None")
            return
        else:
            # prev and next
            prev_node = node.prev
            next_node = node.next
            
            # print prev
            print(prev_node, end="\t <- \t")
            
            # print current
            print(node, end="\t -> \t")
            
            # print next
            print(next_node, end="\t")
            
            if node == self.head:
                print("head")
            elif node == self.tail:
                print("tail")
            else:
                print("")
                
    def debug_print_exiting_nodes(self, msg = None):
            """
                Time Comlexity: O(n)
                memory Complexity: O(1)
                #############################
                this function print all node of linked list
                parameters:
                    msg: the msg you want to print in the first of print nodes
            """
            # print message if found
            if msg:
                print(msg)
                
            
            # pointer
            cur = self.head
            while cur:
                self.debug_print_node(cur)
                cur = cur.next
            print("*" * 60)
    def debug_verify_data_integrity(self):
        """
            this function check the data integrity is correct or not
        """
        # if linked list is empty
        if self.length == 0:
            assert self.head is None
            assert self.tail is None
            return
        # check head and tail
        assert self.head is not None
        assert self.head.prev is None
        assert self.tail is not None
        assert self.tail.next is None
        
        # if has one node
        if self.length == 1:
            assert self.head is self.tail
            
        # if has two nodes
        elif self.length == 2:
            assert self.head.next is self.tail
            
        else:
            assert self.length == len(self.debug_data)
            
            # verify forward pass
            actual_lst_len = 0
            cur = self.head
            while cur:
                cur = cur.next
                actual_lst_len += 1
                assert actual_lst_len < 1000
            
            # check actual length
            assert self.length == actual_lst_len
            
            # verify backword pass
            actual_lst_len = 0
            cur = self.tail
            while cur:
                cur = cur.prev
                actual_lst_len += 1
                assert actual_lst_len < 1000
                
            # check actual length
            assert self.length == actual_lst_len
            
def test1(ll):
    test_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {test_name}")
    
    

if __name__ == '__main__':
    ll = LinkedList([1,2,3,4])
    ll.debug_print_exiting_nodes()