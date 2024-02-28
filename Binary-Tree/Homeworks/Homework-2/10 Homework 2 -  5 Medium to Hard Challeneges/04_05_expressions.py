# https://leetcode.com/problems/height-of-binary-tree/

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, postfix):


        nodes_stk = []

        for char in postfix:
            node = Node(char)

            if not char.isdigit():
                node.right = nodes_stk[-1]  # right first
                node.left = nodes_stk[-2]
                nodes_stk.pop()
                nodes_stk.pop()

            nodes_stk.append(node)

        assert len(nodes_stk) == 1
        self.root = nodes_stk[0]

    def _is_leaf(self, current): # just a number
        return current and not current.left and not current.right

    def _print_inorder_expression(self, current):
        if current.left:
            if not self._is_leaf(current.left):
                print('(', end='')

            self._print_inorder_expression(current.left)

            if not self._is_leaf(current.left):
                print(')', end='')

        print(current.val, end='')

        if current.right:
            if not self._is_leaf(current.right):
                print('(', end='')

            self._print_inorder_expression(current.right)

            if not self._is_leaf(current.right):
                print(')', end='')


    def print_inorder_expression(self):
        self._print_inorder_expression(self.root)
        print()


if __name__ == '__main__':
    tree = BinaryTree('23+4*')
    tree.print_inorder_expression()
    # (2+3)*4

    tree = BinaryTree('51+2/')
    tree.print_inorder_expression()
    # (5+1)/2

    tree = BinaryTree('534*2^+')
    tree.print_inorder_expression()
    # 5+((3*4)^2)
