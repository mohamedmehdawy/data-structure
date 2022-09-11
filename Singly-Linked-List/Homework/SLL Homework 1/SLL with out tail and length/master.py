class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next
        
    def __repr__(self):
        return f"{self.data}"
        

class LinkedList:
    def __init__(self, initial_values=None) -> None:
        self.head = None
        
        if initial_values:
            for value in initial_values:
                self.add_element(value)
    def add_element(self, value):
        node = Node(value)
        
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def get_tail(self):
        temp_head = self.head
        while temp_head and temp_head.next:
            temp_head = temp_head.next
        return temp_head
    def __repr__(self) -> str:
        result = "["
        temp_head = self.head
        while temp_head:
            result += f"{temp_head}{',' if temp_head.next else ''}"
            temp_head = temp_head.next
        result += "]"
        
        return result

def test1(data, expected):
    lst = LinkedList(data)
    lst.add_element(50)
    lst.add_element(10)
    lst.add_element(20)
    
    result = str(lst)
    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")
    
    
def test2(data, expected):
    lst = LinkedList(data)
    lst.add_element(10)
    
    result = str(lst)
    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")
    
def test3(data, expected):
    lst = LinkedList(data)
    
    result = str(lst.get_tail())
    assert result == expected , f"Mismatch between expected=[{expected}] and result=[{result}]"
    print("PASSED")
if __name__ == "__main__":
    test1([], "[20,10,50]")
    test2([], "[10]")
    test3([10, 1, 2, 3], "10")
    print("ALL CASES PASSED")