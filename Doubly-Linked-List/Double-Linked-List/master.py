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
    def _delete_link_node(self, node):
        """
            this function delete delete given node from the linked list
            parameters:
                node: the node will be delete
            return:
                prev: previous of the node
        """
        # check if no node
        if not node:
            return
        
        # check node is tail or node
        is_tail = node == self.tail
        
        # get previous of node
        prev = node.prev
        
        # link prev of next of node
        self._link(prev, node.next)
        
        # delete node for debug and decrease length
        self._delete_node(node)
        
        # check if node is tail
        if is_tail:
            self.tail = prev
        
        # return the prev
        return prev
    

    def _embed_after(self, target, value):
        """
            Time Comlexity: O(1)
            memory Complexity: O(1)
            #############################
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
    
    def delete_node_with_key(self, key):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function delete node with key, it search for node has a same key and delete it
            parameters:
                key: the key will search until found node has same key
        """
        # if linked list empty
        if not self.length:
            return
        else:
            # if the first node has the same key
            if self.head.data == key:
                self.delete_front()
                
            else:
                # search for node
                cur = self.head.next
                
                while cur:
                    if cur.data == key:
                        # delete link node
                        self._delete_link_node(cur)
                    cur = cur.next
        self.debug_verify_data_integrity()
        
    def delete_all_nodes_with_key(self, key):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function delete all node with key, it search for all node with key and delete it
            parameters:
                key: the key will search until found node has same key
        """
        # if emtpy
        if not self.length:
            return
        
        # insert dummy
        self.insert_front(key-1)
        
        # set current the next element of dummy
        cur = self.head.next
        
        while cur:
            if cur.data == key:
                cur = self._delete_link_node(cur)
            cur = cur.next
        # delete dummy node
        self.delete_front()
        self.debug_verify_data_integrity()
    def delete_even_positions(self):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            #############################
            this function delete even positions not values in the linked list in the linked list
        """
        
        if self.length < 2:
            return
        
        # create cur element
        cur = self.head
        
        while cur:
            self._delete_link_node(cur.next)
            cur = cur.next
            
        self.debug_verify_data_integrity()
    def delete_odd_positions(self):
        """
            Time Comlexity: O(n)
            memory Complexity: O(1)
            ##############################
            
            this function delete odd positions not values in the linked list in the linked list
        """
        if self.length < 2:
            return
        
        # append dummy node to call delete even function
        self.insert_front(-1)
        
        # delete even will work well because i add dummy node
        self.delete_even_positions()
        
        # delete the dummy node
        self.delete_front()
        
        self.debug_verify_data_integrity()
        
    def is_palindrome(self):
        """
            this function check if the linked list is palindrome or not
        """
        # check if the length is less than 2 return true
        if self.length < 2:
            return True
        
        # set the half len to divid the list
        half_len = self.length // 2
        
        # set forward and backword
        forward = self.head
        backword = self.tail
        
        while half_len:
            half_len -= 1
            
            # check if forward and backward not have the same value, if true 
            if forward.data != backword.data:
                return False
            
            # move forward and backword
            forward, backword = forward.next, backword.prev
            
        # if leave loop this mean the linked list is palindrome
        return True
    
    def find_the_middle_v1(self):
        """
            this function return the middle of list
            return: value of the middle node
        """
        
        # check if empty
        if not self.head:
            return None
        
        # set forward and backword
        forward, backword = self.head, self.tail
        
        while forward != backword and forward.next != backword:
            forward, backword = forward.next, backword.prev
        
        
        # the middle is the backword
        return backword.data
    
    def find_the_middle_v2(self):   
        """
            this function return the middle of list just using SLL
            return: value of the middle node
        """
        
        # check if empty
        if not self.head:
            return None
        
        # we will use Tortoise and the Hare algorithm
        # slow will walk step by step
        # fast will walk 2 step every once
        slow = fast = self.head
        
        # stop if the fast arraive to the end
        while fast and fast.next:
            
            slow = slow.next # tortoise
            fast = fast.next.next # Hare jump 2 steps
        
        # the middle of the list
        return slow.data
    
    def swap_kth(self, k):
        """
            this function Swap forward with backward
            parameters:
                k: kth node from the front and back of the list
        """
        
        # check if the list is more than one or the k i greater than the length or the list is odd and the k is the middle
        is_odd = self.length % 2 != 0
        if self.length < 2 or k > self.length or (is_odd and k == (self.length // 2) + 1):
            return 
        
        if self.length == 2:
            # change pointers
            self.head.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail.prev = None
            
            # reset head and tail
            self.head, self.tail = self.tail, self.head
            
        else:
            # set first and second
            first, second = self.head, self.tail
            
            # get first and second insted of k
            for _ in range(k-1):
                first, second = first.next, second.prev
            
            # if the first and the second are the same return nothing
            if first is second:
                return
            
            # set next and prev of first and second
            n1,p1,n2,p2 = first.next, first.prev, second.next, second.prev
            
            # swap first and second
            # check if first is next to of second, if true make prev of first is second and the next of second is first
            if first.next is second:
                first.prev = second
                second.next = first
            else:
                first.prev = p2
                second.next = n1

            second.prev = p1
            first.next = n2
            
            # reset prev and next of n1, p1, n2, p2
            if p1 and n2:
                p1.next = second
                n2.prev = first
                
            # check if the next of second is first, if true dont do any thing
            if second.next is not first:
                n1.prev = second
                p2.next = first
            
            # check if the first and second are head and tail, if true reset head and tail
            if first == self.head or first == self.tail:
                # reset head and tail
                self.head, self.tail = self.tail, self.head

        self.debug_verify_data_integrity()
        
    def reverse(self):
        """
            this function reverse the list by addresses
        """
        # check if the list is less than 2 elements
        if self.length < 2:
            return
        
        # set current element is the head
        current = self.head
        
        while current:
            # set the next of the current
            next = current.next
            
            # reset next and prev of the current element
            current.next = current.prev
            current.prev = next
            
            # set current is the next element
            current = next
        
        # reset head and tail
        self.head, self.tail = self.tail, self.head
        
        self.debug_verify_data_integrity()
    
    def merge_2sorted_list(self, other):
        """
            this function merge 2 sorted list in the current list
            parameters:
                other: the other list will merge with the current list
        """
        
        # check if the second list is empty return nothing
        if not other.length:
            return
        
        # set current of two lists
        first_current = self.head
        second_current = other.head
        
        # loop until arrive to the last element in first list or second current
        while first_current and second_current:
            # check if the first current is bigger than the second current
            # if true put the second current in the prev of first current
            # but first set new head of second list
            if first_current.data >= second_current.data:
                # set new head for second list
                other.head = second_current.next
                
                # put second current in the first list
                self._link(first_current.prev, second_current)
                self._link(second_current, first_current)
                
                # check if the first current is the head set the new head
                if first_current == self.head:
                    self.head = second_current # prev of first current
            else:
                # move the first current
                first_current = first_current.next
            # reset second current
            second_current = other.head
            
        # check if we have some elements in the second list
        if other.length:
            # append each element of second list to the first one
            while second_current:
                # set new value of second list head
                other.head = second_current.next

                # append the second current in the end of first list
                if self.tail:
                    self._link(second_current, self.tail.next)
                    self._link(self.tail, second_current)
                else:
                    # link second current with None
                    self._link(second_current, None)
                    self._link(None, second_current)

                    # reset head and tail of first node
                    self.head = self.tail = second_current
                    
                # increase length
                self._add_node(second_current)
                
                # move the tail
                self.tail = second_current
                
                # move the second current
                second_current = other.head
                

        # reset second list tail
        other.tail = None
        
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
            assert self.length == actual_lst_len, f"from head, lenght: {self.length}, actual: {actual_lst_len}"
            
            # verify backword pass
            actual_lst_len = 0
            cur = self.tail
            while cur:
                cur = cur.prev
                actual_lst_len += 1
                assert actual_lst_len < 1000
                
            # check actual length
            assert self.length == actual_lst_len, f"from tail, lenght: {self.length}, actual: {actual_lst_len}"
            
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
    
    print(f"testing: {fun_name} -> insert_end")
    
    ll = LinkedList(data)
    ll.insert_end(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"


def test2(data, value, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> insert_front")
    
    ll = LinkedList(data)
    ll.insert_front(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test3(data, value, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> insert_sorted")
    
    ll = LinkedList(data)
    ll.insert_sorted(value)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test4(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_front")
    
    ll = LinkedList(data)
    ll.delete_front()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test5(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_back")
    
    ll = LinkedList(data)
    ll.delete_back()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test6(data, key, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_node_with_key")
    
    ll = LinkedList(data)
    ll.delete_node_with_key(key)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"


def test7(data, key, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_all_nodes_with_key")
    
    ll = LinkedList(data)
    ll.delete_all_nodes_with_key(key)
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"


def test8(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_even_positions")
    
    ll = LinkedList(data)
    ll.delete_even_positions()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test9(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> delete_odd_positions")
    
    ll = LinkedList(data)
    ll.delete_odd_positions()
    
    assert str(ll) == expected, f"Mismatch between expected={expected}, and result={ll} in {fun_name}"

def test10(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> is_palindrome")
    
    ll = LinkedList(data)
    result = ll.is_palindrome()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

def test11(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> find_the_middle_v1")
    
    ll = LinkedList(data)
    result = ll.find_the_middle_v1()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

def test12(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> find_the_middle_v2")
    
    ll = LinkedList(data)
    result = ll.find_the_middle_v2()
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

def test13(data, k,expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> swap_kth")
    
    ll = LinkedList(data)
    ll.swap_kth(k)
    result = str(ll)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

def test14(data, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> reverse")
    
    ll = LinkedList(data)
    ll.reverse()
    result = str(ll)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

def test15(l1, l2, expected):
    fun_name = inspect.currentframe().f_code.co_name
    
    print(f"testing: {fun_name} -> merge_2sorted_list")
    
    ll = LinkedList(l1)
    l2 = LinkedList(l2)
    ll.merge_2sorted_list(l2)
    result = str(ll)
    
    assert result == expected, f"Mismatch between expected={expected}, and result={result} and linked list is {ll} in {fun_name}"

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

    # # test 5
    # test5([], "[]")
    # test5([1], "[]")
    # test5([1,2], "[1]")
    # test5([1,2,3,4,5,6], "[1,2,3,4,5]")

    # # test 6
    # test6([], 1, "[]")
    # test6([1,2,3], 1, "[2,3]")
    # test6([1,2,3,4], 2, "[1,3,4]")
    # test6([1,2,3,4], 4, "[1,2,3]")
    
    
    # test 7
    # test7([], 1, "[]")
    # test7([1,2,3], 1, "[2,3]")
    # test7([1,2,3], 2, "[1,3]")
    # test7([1,2,3], 3, "[1,2]")
    # test7([1,1,1,1,2,3,4,1,1,5,1], 1, "[2,3,4,5]")
    # test7([2,3,4,1,1,5,1], 1, "[2,3,4,5]")
    # test7([2,3,4,5,1], 1, "[2,3,4,5]")

    # test 8
    # test8([], "[]")
    # test8([1], "[1]")
    # test8([1,2], "[1]")
    # test8([1,2,3], "[1,3]")
    # test8([1,2,3,4], "[1,3]")
    # test8([1,2,3,4,5], "[1,3,5]")
    # test8([1, 2, 3, 4, 10], "[1,3,10]")
    # test8([1, 2, 3, 4, 5, 6], "[1,3,5]")
    
    # test 9
    # test9([], "[]")
    # test9([1], "[1]")
    # test9([1,2], "[2]")
    # test9([1,2,3], "[2]")
    # test9([1,2,3,4], "[2,4]")
    # test9([1, 2, 3, 4, 10], "[2,4]")
    # test9([1, 2, 3, 4, 5, 7], "[2,4,7]")
    
    # test 10
    # test10([], True)
    # test10([1], True)
    # test10([1,1], True)
    # test10([1,2,3,2,1], True)
    # test10([1,2,1], True)
    # test10([1,2], False)
    # test10([1,2,3,1], False)
    
    # test 11
    # test11([], None)
    # test11([1], 1)
    # test11([1,2], 2)
    # test11([1,2,3], 2)
    # test11([1,2,3,4,5], 3)
    # test11([1,2,3,4,5,6], 4)
    
    # test 12
    # test12([], None)
    # test12([1], 1)
    # test12([1,2], 2)
    # test12([1,2,3], 2)
    # test12([1,2,3,4,5], 3)
    # test12([1,2,3,4,5,6], 4)
    
    # test 13
    # test13([], 1, "[]")
    # test13([1,2,3,4,5,6], 20, "[1,2,3,4,5,6]")
    # test13([1,2], 1, "[2,1]")
    # test13([1,2,3], 1, "[3,2,1]")
    # test13([1,2,3], 2, "[1,2,3]")

    # test13([1,2,3,4,5,6], 1, "[6,2,3,4,5,1]")
    # test13([1,2,3,4,5,6], 2, "[1,5,3,4,2,6]")
    # test13([1,2,3,4,5,6], 3, "[1,2,4,3,5,6]")
    # test13([1,2,3,4], 2, "[1,3,2,4]")
    
    # test 14 => reverse
    # test14([], "[]")
    # test14([1], "[1]")
    # test14([1,2], "[2,1]")
    # test14([1,2,3], "[3,2,1]")
    # test14([1,2,3,4,5,6], "[6,5,4,3,2,1]")
    
    # test 15 => merge_2sorted_list
    test15([1,2], [], "[1,2]")
    test15([], [1], "[1]")
    test15([], [1,2,3], "[1,2,3]")

    # all passed
    print("all tests passed")