class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)

        current = self.root
        # iterate on the path, all necessary nodes
        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.val == values_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right

    def _traverse_left_boundry(self, current):
        if not current:
            return []

        if current.left:
            ans = self._traverse_left_boundry(current.left)
        else:   # Go o the right IFF no left
            ans = self._traverse_left_boundry(current.right)

        ans.append(current.val)
        return ans

    def traverse_left_boundry(self):    # O(n) time
        res = self._traverse_left_boundry(self.root)
        return res[::-1]    # list is reversed


def test1():
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    assert tree.traverse_left_boundry() == [1, 2, 4, 7]


def test2():
    tree = BinaryTree(1)

    tree.add([2, 4, 5, 6, 7, 9, 11], ['L', 'L', 'R', 'R', 'L', 'L', 'R'])
    tree.add([2, 4, 5, 6, 8], ['L', 'L', 'R', 'R', 'R'])
    tree.add([2, 4, 5, 6, 7, 10], ['L', 'L', 'R', 'R', 'L', 'R'])
    tree.add([3], ['R'])

    assert tree.traverse_left_boundry() == [1, 2, 4, 5, 6, 7, 9, 11]

if __name__ == '__main__':
    test1()
    test2()



