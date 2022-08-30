class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1= Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
# print(node1)
# print(node2)
# print(node3)
# print(node1.next)
# print(node2.next)
# print(node3.next)

print(id(node1))
print(id(node1.next))
print(id(node2))
print(id(node2.next))
print(id(node3))
# print(id(node3.next))