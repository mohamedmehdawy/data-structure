import inspect


class Node:
    def __init__(self, index, data=None, next=None, prev=None):
        self.data = data
        self.index = index
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'{self.data}@{self.index}'


class SparseArray:
    def __init__(self, array_length):
        # Dummy node of index = -1, to make coding shorter and more robust!
        self.tail = self.head = Node(-1, None)
        self.length = 1         # total number of nodes
        self.array_length = array_length

    @staticmethod
    def _link(first, second):
        if first:
            first.next = second
        if second:
            second.prev = first

    def _embed_after(self, node, index, data=None):
        # Add a node with value between node and its next
        new_node = Node(index, data)
        self.length += 1
        self._link(new_node, node.next)
        self._link(node, new_node)

        return new_node

    # Return the node of this index
    def get_node(self, index, is_create_if_missing=True):
        # Find the largest node where node.index < index
        prev = self.head
        while prev.next and prev.next.index < index:
            prev = prev.next

        if prev.next and prev.next.index == index:  # found
            return prev.next

        if not is_create_if_missing:
            return None

        return self._embed_after(prev, index, None)

    def set_value(self, index, data):
        assert 0 <= index < self.array_length
        self.get_node(index, True).data = data

    def get_value(self, index):
        assert 0 <= index < self.array_length
        node = self.get_node(index, False)
        if not node:
            return None
        return node.data

    def add(self, other):  # O(Nodes1 * Nodes2)
        assert self.array_length == other.array_length
        if not self.array_length:
            return

        # Iterate on the other first, add it to the current one
        h = other.head.next
        while h:
            node = self.get_node(h.index, True)
            if node.data is None:
                node.data = h.data
            else:
                node.data += h.data
            h = h.next
    
    def __repr__(self):
        represent = ''
        cur = self.head.next

        while cur is not None:
            represent += str(cur)
            cur = cur.next
            if cur:
                represent += ', '

        return represent

    def print_as_array(self):
        cur = self.head.next

        for c in range(self.array_length):
            if cur and cur.index == c:
                print(cur.data, end=' ')
                cur = cur.next
            else:
                print(0, end=' ')
        print()


def test1():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)
    array.set_value(5, 50)  # idx, value
    array.set_value(2, 20)
    array.set_value(8, 80)
    array.set_value(4, 4000)
    array.set_value(4, 40)

    result = str(array)
    expected = '20@2, 40@4, 50@5, 80@8'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test2():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)
    array.set_value(5, 'Mostafa')  # idx, value
    array.set_value(2, 20)

    result = str(array)
    expected = '20@2, Mostafa@5'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test3():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)
    array.set_value(5, 50)
    array.set_value(2, 20)
    array.set_value(8, 80)
    array.set_value(4, 4000)
    array.set_value(4, 40)

    array2 = SparseArray(15)
    array2.set_value(5, 3)
    array2.set_value(14, 100)

    array.add(array2)

    result = str(array)
    expected = '20@2, 40@4, 53@5, 80@8, 100@14'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test4():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)

    array2 = SparseArray(15)
    array2.set_value(5, 3)
    array2.set_value(14, 100)

    array.add(array2)

    result = str(array)
    expected = '3@5, 100@14'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test5():
    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)
    array.set_value(5, 3)
    array.set_value(14, 100)

    array2 = SparseArray(15)


    array.add(array2)

    result = str(array)
    expected = '3@5, 100@14'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def test6():
    # Be careful with customer requirements. Why not add strings? or any addable object?

    func_name = inspect.currentframe().f_code.co_name
    print(f'Testing {func_name}')

    array = SparseArray(15)
    array.set_value(0, 'Most')
    array.set_value(2, 'Ibrahim')

    array2 = SparseArray(15)
    array2.set_value(0, 'afa')
    array2.set_value(1, 'Saad')


    array.add(array2)

    result = str(array)
    expected = 'Mostafa@0, Saad@1, Ibrahim@2'

    assert result == expected, f'Mismatch between expected=[{expected}] and result=[{result}] in {func_name}'
    print('PASSED\n')


def driver():
    array = SparseArray(15)
    array.set_value(5, 50)  # idx, value
    array.set_value(2, 20)
    array.set_value(8, 80)
    array.set_value(4, 4000)
    array.set_value(4, 40)

    print(array.get_value(8), array.get_value(9))
    # 80 None

    print(array)
    # 20@2, 40@4, 50@5, 80@8

    array.print_as_array()
    # 0 0 20 0 40 50 0 0 80 0 0 0 0 0 0

    array2 = SparseArray(15)
    array2.set_value(5, 3)
    array2.set_value(14, 100)

    print(array2)
    # 3@5, 100@14
    array.add(array2)
    print(array)
    # 20@2, 40@4, 53@5, 80@8, 100@14


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

    driver()
    # Must see to insure no RTE
    print('ALL CASES PASSED')

