class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def _print_inorder(self, current):
        if not current:
            return
        self._print_inorder(current.left)
        print(current.val, end=' ')
        self._print_inorder(current.right)

    def print_inorder(self):
        self._print_inorder(self.root)

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

    def inorder_iterative(self):
        # Pair: node and it has been expanded or not so far
        nodes_stk = []

        # Just convert the recursion to calls.
        nodes_stk.append([self.root, False])
        res = []

        while nodes_stk:
            current, is_completed = nodes_stk[-1]
            nodes_stk.pop()

            # If expanded already and we are here, we just returned from recursion. Print
            if is_completed:
                res.append(current.val)
            else:
                # Push your children and mark yourself as expanded
                # Observe: put right, left as stack verse things. We need left prossed first
                if current.right:
                    nodes_stk.append([current.right, False])

                nodes_stk.append([current, True])

                if current.left:
                    nodes_stk.append([current.left, False])

        return res
        # There is another way for self problem based on tracing the nodes in order
        # e.g. keep expand left and add to stack
        # But approach here is nicer as it follows the recurrance itself generic style


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    #tree.print_inorder()
    # 7 4 8 2 5 9 1 3 10 6

    assert tree.inorder_iterative() == [7, 4, 8, 2, 5, 9, 1, 3, 10, 6]


