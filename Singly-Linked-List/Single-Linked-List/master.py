class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"{self.data}"
def print_lst(head):
    if head is not None:
        print(head.data, end="->")
        print_lst(head.next)

def print_lst_reversed(head):
    if head is not None:
        print_lst_reversed(head.next)
        print(head.data, end="->")

def search(head, value):
    while head is not None:
        if head.data == value:
            return head
        head = head.next
    
    return None

node1= Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

print(search(node1, 3))
print_lst_reversed(node1)
# print(node1)
# print(node2)
# print(node3)
# print(node1.next)
# print(node2.next)
# print(node3.next)

# print(id(node1))
# print(id(node1.next))
# print(id(node2))
# print(id(node2.next))
# print(id(node3))
# print(id(node3.next))