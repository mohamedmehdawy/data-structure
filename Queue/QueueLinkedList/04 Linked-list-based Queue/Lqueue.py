class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_end(self, value):
        node = Node(value)
        self.length += 1

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_front(self):                 # O(1) time - O(1) memory
        if not self.head:
            return

        value = self.head.data
        next = self.head.next
        self.length -= 1
        self.head = next

        if self.length <= 1:
            self.tail = self.head

        return value

    def __repr__(self):
        represent = ''
        temp_head = self.head

        while temp_head is not None:
            represent += str(temp_head.data)
            temp_head = temp_head.next
            if temp_head:
                represent += ', '

        return represent


class Queue:
    def __init__(self):
        self.lst = LinkedList()

    def enqueue(self, value):
        self.lst.insert_end(value)

    def dequeue(self):
        assert not self.empty()
        return self.lst.delete_front()

    def empty(self):
        return self.lst.length == 0

    def display(self):
        if self.empty():
            print("EMPTY\n")
        else:
            print(self.lst)


if __name__ == '__main__':

    qu = Queue()

    assert qu.empty()
    qu.display()

    for i in range(1, 7):
        qu.enqueue(i)
        qu.display()

    print()

    for i in range(1, 7):
        assert not qu.empty()
        qu.dequeue()
        qu.display()

    print()


'''
EMPTY

1
1, 2
1, 2, 3
1, 2, 3, 4
1, 2, 3, 4, 5
1, 2, 3, 4, 5, 6

2, 3, 4, 5, 6
3, 4, 5, 6
4, 5, 6
5, 6
6
EMPTY



'''
