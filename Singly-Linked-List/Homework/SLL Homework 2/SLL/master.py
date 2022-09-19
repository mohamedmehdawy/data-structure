

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
        if self.head:
            if self.head == self.tail:
                self._delete_node(self.head)
                self.head = self.tail = None
            else: 
                prev = self.head
                while prev.next != self.tail:
                    prev = prev.next
                self._delete_node(self.tail)
                self.tail = prev
                prev.next = None
    def delete_nth(self, n):
        """
            Time: O(n)
            memory: O(1)
        """
        if self.length and n <= self.length and n > 0:
            if n == 1:
                self.delete_front()
            elif n == self.length:
                self.delete_back()
            else:
                current = self.head
                prev = None
                count = 1
                while count != n:
                    prev = current
                    current = current.next
                    count += 1
                prev.next = current.next
                self._delete_node(current)
    def delete_value(self, value):
        """
            Time: O(n)
            Memory: O(1)
        """
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
    lst.delete_value(1)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    lst._debug_verify_data_integrity()

    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")

def test2(data, expected):
    lst = LinkedList(data)
    lst.delete_value(2)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    lst._debug_verify_data_integrity()

    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")
    

def test3(data, expected):
    lst = LinkedList(data)
    lst.delete_value(5)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    lst._debug_verify_data_integrity()

    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")

def test4(data, expected):
    lst = LinkedList(data)
    lst.delete_value(20)
    result = str(lst)
    print(lst._debug_print_exsiting_nodes())
    lst._debug_verify_data_integrity()

    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")


if __name__ == "__main__":
    test1([1, 2, 3], "[2,3]")
    test2([1, 2, 3], "[1,3]")
    test3([1, 2,3,4,5], "[1,2,3,4]")
    test4([1, 2,3,4,5], "[1,2,3,4,5]")

    
    print("ALL CASES PASSED")
