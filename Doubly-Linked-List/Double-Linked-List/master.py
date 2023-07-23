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
    def _delete_node(self, node):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function delte node to debug data and increase length
            parameters:
                node: will be added to debug data
        """
        self.debug_data.remove(node)
        del node
        self.length -= 1
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
        
    def _embed_after(self, target, value):
        """
            this function instert new node with value after target node
            parameters:
                target: the target node will insert the new node after it
                value: the value of node will add after target
        """
        # new node
        node = Node(value)
        
        # after target
        after = target.next
        
        # link node with after
        self._link(node, after)
        
        # link target with node
        self._link(target, node)
        
        # add node
        self._add_node(node)
    def insert_end(self, value):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function insert node to the end of linked list
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
    def insert_front(self, value):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function insert node to the front of linked list
            parameters:
                value: the value will add in the front of linked list as npde
        """
        # create node
        node = Node(value)
        
        # if linked list is empity
        if self.length == 0:
            self.head = self.tail = node
        else:
            self._link(node, self.head)
            self.head = node
        # add node
        self._add_node(node)
        
        self.debug_verify_data_integrity()
    
    def insert_sorted(self, value):
        """
            this function insert node with sorted
            paramerts:
                value: the value will add to linked list with sorted as node
        """
        
        # if linked list is empty or the value is less than head
        if not self.length or value <= self.head.data :
            self.insert_front(value)
        
        # if the value is greater than the tail data
        elif value >= self.tail.data:
            self.insert_end(value)
            
        # search for the node is less than the value
        else:
            cur = self.head.next

            while cur:
                if cur.data >= value:
                    self._embed_after(cur.prev, value)
                    break
                cur = cur.next
        self.debug_verify_data_integrity()
        
    def delete_front(self):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function delete first node from linked list
        """
        if not self.length:
            return
        else:
            # next node of head
            new_head = self.head.next

            # delete node
            self._delete_node(self.head)
            
            # move head
            self.head = new_head
        
            
            # check if is last node or linked list is empty
            if not self.length:
                self.tail = self.head # will be None
            # set head prev to be none
            else:
                self.head.prev = None
        self.debug_verify_data_integrity()
    
    def delete_back(self):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
            this function delete last node (tail)
        """
        if self.length <= 1:
            self.delete_front()
            return
        else:
            # get new tail
            new_tail = self.tail.prev
            
            # remove tail
            self._delete_node(self.tail)
            
            # set tail
            self.tail = new_tail
            
            # fix next of tail
            self.tail.next = None
            
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
            
    def __repr__(self):
        """
            function repr to print nodes when print linked list
        """
        result = "["
        
        cur = self.head
        
        while cur:
            result += f"{str(cur) + ',' if cur.next else str(cur)}"
            cur = cur.next
        result += "]"
        
        return result
    def print(self):
        """
            this function print nodes and start from head
        """
        cur = self.head
        
        while cur:
            print(f"{str(cur)} -> ", end="")
            cur = cur.next
        
        print("None")
    def print_reversed(self):
        """
            this functoin print node but start from tail
        """
        
        
        cur = self.tail
        
        while cur:
            print(f"{str(cur)} -> ", end="")
            cur = cur.prev
        
        print("None")
        
    def __iter__(self):
        """
            make linked list iterable
        """

        cur = self.head
        while cur:
            yield cur
            cur = cur.next
def test1(data, value, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {fun_name} -> insert_end")
    
    ll = LinkedList(data)
    ll.insert_end(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"


def test2(data, value, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {fun_name} -> insert_front")
    
    ll = LinkedList(data)
    ll.insert_front(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test3(data, value, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {fun_name} -> insert_sorted")
    
    ll = LinkedList(data)
    ll.insert_sorted(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test4(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {fun_name} -> delete_front")
    
    ll = LinkedList(data)
    ll.delete_front()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test5(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testting: {fun_name} -> delete_back")
    
    ll = LinkedList(data)
    ll.delete_back()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

if __name__ == '__main__':
    
    # # test 1
    # test1([], 1, "[1]")
    # test1([1,2,3,4], 5, "[1,2,3,4,5]")
    
    # # test 2
    # test2([], 1, "[1]")
    # test2([1,2,3,4], 5, "[5,1,2,3,4]")

    # # test 3
    # test3([], 1, "[1]")
    # test3([10,10.5,15], 11, "[10,10.5,11,15]")
    # test3([10,20,30,40], 5, "[5,10,20,30,40]")
    # test3([10,20,30,40], 35, "[10,20,30,35,40]")
    # test3([10,20,30,40], 50, "[10,20,30,40,50]")

    # # test 4
    # test4([], "[]")
    # test4([1], "[]")
    # test4([1,2,3,4], "[2,3,4]")

    # test 5
    test5([], "[]")
    test5([1], "[]")
    test5([1,2], "[1]")
    test5([1,2,3,4,5,6], "[1,2,3,4,5]")

    # all passed
    print("all tests passed")