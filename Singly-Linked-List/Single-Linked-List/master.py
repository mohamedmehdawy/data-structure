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
    
    def insert_end(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print()
        

ll = LinkedList()

for n in range(5):
    ll.insert_end(n)

ll.print_list()