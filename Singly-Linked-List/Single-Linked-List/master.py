class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self) -> str:
        return f"{self.data}"
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def get_nth(self, n):
        if n <= self.length:
            current = self.head
            for _ in range(n - 1):
                current = current.next
            return current
        return None

    def index(self, value):
        temp_head = self.head
        idx = 0
        while temp_head:
            if temp_head.data == value:
                return idx
            temp_head = temp_head.next
            idx += 1
        return -1
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        

ll = LinkedList()

ll.insert_end(6)
ll.insert_end(10)
ll.insert_end(8)
ll.insert_end(15)

for value in [6, 10, 8, 15, 99]:
    print(f"index of {value} => {ll.index(value)}")