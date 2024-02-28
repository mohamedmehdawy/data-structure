# https://leetcode.com/problems/height-of-binary-tree/

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


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, current):
        if not current:
            return 0

        lheight = self.height(current.left)
        rheight = self.height(current.right)

        # maximize the global diameter with the diameter
        # PASSING with this node
        self.diameter = max(self.diameter, lheight + rheight)

        return 1 + max(lheight, rheight)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 15], ['R', 'R', 'L'])

    sol = Solution()
    assert sol.diameterOfBinaryTree(tree.root) == 6
