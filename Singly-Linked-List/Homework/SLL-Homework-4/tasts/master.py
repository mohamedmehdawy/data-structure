

class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

    def __repr__(self) -> str:
        return f"{self.data}"
    

class LinkedList:
    def __init__(self, init_values=None):
        self.head = None
        self.tail = None
        self.length = 0
        self._debug_data = []
        if init_values: 
            for value in init_values:
                self.insert_end(value)
    def _add_node(self, node):
        self._debug_data.append(node)
        self.length += 1
    def _delete_node(self, node):
        self._debug_data.remove(node)
        del node
        self.length -= 1
    def get_previous(self, node):
        """
            this function return previous of node
            parameters:
                node: you need to get previous of it
            return:
                previous of node
        """
        temp = self.head
        while temp.next:
            if temp.next == node:
                return temp
            temp = temp.next
        return None
    def insert_front(self, value):
        """
            Time: O(1)
            Memory: O(1)
        """
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._add_node(node)
        self._debug_verify_data_integrity()
        
    def insert_end(self, value):
        """
            Time: O(1)
            Memory: O(1)
        """
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._add_node(node)
    def delete_front(self):
        """
            Time: O(1)
            Memory: O(1)
        """
        if self.head:
            node = self.head
            self.head = self.head.next
            self._delete_node(node)
            if self.length < 1:
                self.tail = self.head
    def delete_back(self):
        """
            Time: O(n)
            memory: O(1)
        """
        if self.length <= 1:
            self.delete_front()
            return
        else: 
            prev = self.get_nth(self.length - 1)
            self._delete_node(self.tail)
            self.tail = prev
            self.tail.next = None
    def delete_nth(self, n):
        """
            Time: O(n)
            memory: O(1)
        """
        if n <= self.length and n > 0:
            if n == 1:
                self.delete_front()
            elif n == self.length:
                self.delete_back()
            else:
                prev = self.get_nth(n - 1)
                current = prev.next
                prev.next = current.next
                self._delete_node(current)
                
        else:
            print("Error. No such nth node")
    def delete_value(self, value):
        if self.length:
            prev = None
            current = self.head
            
            while current:
                if current.data == value:
                    break
                prev = current
                current = current.next
            if current:
                if current == self.head:
                    self.delete_front()
                elif current == self.tail:
                    self.delete_back()
                else:
                    prev.next = current.next
                    self._delete_node(current)
                return                
        return f"value=>{value}, is not found"
    def delete_next(self, prev):
        """
            this function delete next node
            Time: O(1)
            Memory: O(1)
        """
        node = prev.next
        if node == self.tail:
            self.delete_back()
        else:
            prev.next = node.next
            self._delete_node(node)
    def remove_duplicates_from_not_sorted(self):
        # if elements less than 2
        if self.length < 2:
            return
        else:
            # target element
            target = self.head
            
            while target and target.next:
                prev = target
                current = target.next
                while current:
                    if target.data == current.data:
                        self.delete_next(prev)
                        current = prev.next
                    else:
                        prev = current
                        current = current.next
                target = target.next
                
                
    def delete_last_occurance(self, target):
        """
            -----------------------
            Time: O(n)
            Memory: O(1)
            -----------------------
            this function delete last occurance insted of target
            params:
                target: will be delete the last of it
            return: None
        """
        if self.length < 2:
            return
        else:
            # current element
            current = self.head
            # prev of target and set first node if target = it
            prev_target = current if target == current.data else None
            
            while current.next:
                if current.next.data == target:
                    prev_target = current
                current = current.next
                
            # check if prev target is found
            if prev_target:
                # if still target first node remove first node
                if prev_target == self.head:
                    self.delete_front()
                else:
                    # remove next element of prev target
                    self.delete_next(prev_target)

    def get_nth(self, n):
        if n <= self.length:
            current = self.head
            for _ in range(n - 1):
                current = current.next
            return current
        return None
    def get_nth_back(self, n):
        """
            Time: O(n)
            Memeory: O(1)
        """
        return self.get_nth(self.length - n + 1)
    
    def is_identical_data(self, ll):
        """
            Time: O(n)
            Memery: O(1)
        """
        h1, h2 = self.head, ll.head
        
        while h1 and h2:
            if h1.data != h2.data:
                return False
            h1, h2 = h1.next, h2.next
        return not h1 and not h2
    def index(self, value):
        temp_head = self.head
        idx = 0
        while temp_head:
            if temp_head.data == value:
                return idx
            temp_head = temp_head.next
            idx += 1
        return -1
    
    def index_transposition(self, value):
        temp_head = self.head
        prev = None
        idx = 0
        while temp_head:
            if temp_head.data == value:
                if prev:
                    temp_head.data, prev.data = prev.data, temp_head.data
                    return idx - 1
                return idx
            prev = temp_head
            temp_head = temp_head.next
            idx += 1
        return -1

    def swap_head_tail(self):
        """
            time: O(n)
            memory: O(1)
        """
        if self.length < 2:
            return
        
        # if length is = 2
        elif self.length == 2:
            # set tail.next to self.head
            self.tail.next = self.head
        
        # if is more than 2 elements
        else:

            # set tail.next to the next of head
            self.tail.next = self.head.next
            
            # get prev tail element
            prev_tail = self.get_previous(self.tail)
            
            # set prev tail next = the head
            prev_tail.next = self.head
        # make next of head = none, and swap head and tail
        self.head.next = None
        self.head, self.tail = self.tail, self.head
        
        self._debug_verify_data_integrity()
    
    def right_rotate(self, k):
        """
            ######################
            Time: O(n)
            Memoery: O(1)
            ######################
            this function right rotate insted of k time
            parameters:
                k: number of rotates
            return:
                None
        """
        # number of iteration
        iteration = k % self.length
        # if have 1 or 0 elements
        if self.length < 2 or iteration == 0:
            return
        # if have more than 1
        else:
            # get nth
            nth = self.get_nth(iteration)
            # set tail.next = head
            self.tail.next = self.head
            # set head
            self.head = nth.next
            # set tail
            self.tail = nth
            # set tail.next= None
            self.tail.next = None
        self._debug_verify_data_integrity()
        
    def left_rotate(self, k):
        """
            ######################
            Time: O(n)
            Memoery: O(1)
            ######################
            this function left roate insted of k time
            parameters:
                k: number of rotates
            return:
                None
        """
        # number of iteration
        iteration = k % self.length
        
        if self.length < 2 or iteration == 0:
            return
        else:
            # get nth
            nth = self.get_nth(self.length - iteration)
            
            # make tail next is head
            self.tail.next = self.head
            
            # make head = next nth
            self.head = nth.next
            
            # make tail = prev tail
            self.tail = nth
            
            # reset next of tail
            self.tail.next = None

        self._debug_verify_data_integrity()

        
    def _move_to_back(self, prev, cur):
        """
            this function move element to the end
            parameters:
                prev: previous of current
                cur: the current element
            return:
                next of current
        """
        next = cur.next
        
        # check if current is head
        if prev:
            prev.next = next
        else:
            self.head = next
        
        # move current to the end
        self.tail.next = cur
        self.tail = cur
        self.tail.next = None
        return next
    def move_the_back(self, key):
        """
            this function move any element is same key to the end
            parameters:
                key: target
            return: None
        """
        if self.length < 2:
            return
        else:
            # step
            step = 1
            
            # count of shift
            count = 0
            
            # prev and current of element
            current = self.head
            prev = None

            while self.length - count >= step:

                if current.data == key:
                    # move current and set current to next
                    current = self._move_to_back(prev, current)
                    
                    # increase count
                    count += 1
                else:
                    prev, current = current, current.next
                # increase step
                step += 1
        self._debug_verify_data_integrity()
    def _debug_verify_data_integrity(self):
        if self.length == 0:
            assert self.head == None
            assert self.tail == None
            return
        
        assert self.head != None
        assert self.tail != None
        assert self.tail.next == None
        
        if self.length == 1:
            assert self.head == self.tail
        elif self.length == 2:
            assert self.head.next == self.tail
        else:
            temp_head = self.head
            counter = 0
            
            while temp_head:
                temp_head = temp_head.next
                counter += 1
                assert counter < 1000
                
            assert self.length == counter
            # assert self.length == len(self._debug_data)
        
        return "all is good"
    def _debug_print_exsiting_nodes(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += f"{temp_head}\t->\t{temp_head.next}"
            if temp_head == self.head:
                result += "\t head"
            elif temp_head.next == None:
                result += "\t tail"
            result += "\n"
            temp_head = temp_head.next

        result += "*" * 30
        return result
    
    def _debug_print_address(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += f"{id(temp_head)}\t->\t{id(temp_head.next) if temp_head.next else temp_head.next}"
            if temp_head == self.head:
                result += "\t head"
            elif temp_head.next == None:
                result += "\t tail"
            result += "\n"
            temp_head = temp_head.next

        result += "*" * 30
        return result

    def __repr__(self) -> str:
        result = "["
        temp_head = self.head
        for i in range(self.length):
            result += f"{temp_head}{',' if i < self.length - 1 else ''}"
            temp_head = temp_head.next
        result += "]"
        return result

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        

def test1(data, expected):
    lst = LinkedList(data)
    print("-" * 50)
    print(lst._debug_print_exsiting_nodes())
    print(lst._debug_print_address())

    lst.remove_duplicates_from_not_sorted()
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    print(lst._debug_print_address())
    print("-" * 50)
    lst._debug_verify_data_integrity()

    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")

def test2(data, target, expected):
    lst = LinkedList(data)
    lst.delete_last_occurance(target)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    
    assert result == expected, f"Mismatch between expected=[{expected}] and result=[{result}]"
    
    print("PASSED")
    
def test3(data, target, expected):
    lst = LinkedList(data)
    lst.move_the_back(target)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    
    assert result == expected, f"Mismatch between expected=[{expected}] and result=[{result}]"
    
    print("PASSED")
    
def test4(data, number,expected):
    lst = LinkedList(data)
    lst.left_rotate(number)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    
    assert result == expected, f"Mismatch between expected=[{expected}] and result=[{result}]"
    
    print("PASSED")

def test5(data, number,expected):
    lst = LinkedList(data)
    lst.right_rotate(number)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    
    assert result == expected, f"Mismatch between expected=[{expected}] and result=[{result}]"
    
    print("PASSED")
    
    
def test6(data, expected):
    lst = LinkedList(data)
    print(lst._debug_print_address())
    lst.swap_head_tail()
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    print(lst._debug_print_address())
    
    assert result == expected, f"Mismatch between expected=[{expected}] and result=[{result}]"
    
    print("PASSED")

if __name__ == "__main__":
    # test1([1,1, 2, 1, 3, 2, 4, 3, 5], "[1,2,3,4,5]")
    # test1([1, 2, 3, 4, 5], "[1,2,3,4,5]")
    # test1([1, 1, 1], "[1]")

    # test2([1,2,3], 1, "[2,3]")
    # test2([1,2,3,4], 1, "[2,3,4]")
    # test2([1,2,3,1,4], 1, "[1,2,3,4]")
    # test2([1,2,3,4], 7, "[1,2,3,4]")

    test3([1, 2, 3, 2, 4, 1], 1, "[2,3,2,4,1,1]")
    test3([1, 2, 3, 1, 2, 4, 1, 7, 1, 8, 1, 1], 1, "[2,3,2,4,7,8,1,1,1,1,1,1]")
    
    # test4([6, 10, 8, 15], 4, "[6,10,8,15]")
    # test4([6, 10, 8, 15], 6, "[8,15,6,10]")
    # test4([6, 10, 8, 15, 1], 2, "[15,1,6,10,8]")
    # test6([1,2], "[2,1]")
    # test6([1,2,3,4,5], "[5,2,3,4,1]")
    print("ALL CASES PASSED")