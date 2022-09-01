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

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
        

ll = LinkedList()

for n in range(5):
    ll.insert_end(n)

for item in ll:
    print(item)