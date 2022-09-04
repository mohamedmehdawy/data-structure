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

    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next
        

ll = LinkedList()

for n in range(5):
    ll.insert_end(n)

for item in ll:
    print(item)
    

print(f"length => {len(ll)}")
print(ll.get_nth(5))