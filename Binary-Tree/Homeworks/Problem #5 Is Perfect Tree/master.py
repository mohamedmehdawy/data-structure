class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)
        # length will start with 1, because we already add the root node
        self.length = 1

    def add(self, nodes, directions):
        """
            this function add nodes to the binary insted of his directions
            parameters:
                nodes: the nodes will added to the binary
                directions: the direction of the nodes
        """
        # init current
        current = self.root
        # loop insted of the index
        for index in range(len(nodes)):
            current = self.add_node(current, nodes[index], directions[index])

    def add_node(self, current, value, direction):
        """
            this function link the node insted of his direction
            parameters:
                current: the current node will linked with the target node
                value: the value of current or new node
                direction: the direction of the linked (left or right)
        """
        # increase the length
        # if the direction is left
        if direction == "L":
            if not current.left:
                # create new node and link with current.left
                current.left = Node(value)
                self.length += 1

            else:
                assert current.left.data == value
                self.length += 1

            return current.left

        # if the direction is right
        if not current.right:
            # create new node and link with current.right
            current.right = Node(value)
        else:
            assert current.right.data == value
        return current.right

    def print_inorder(self):
        """
            this function print the tree in inorder way
        """
        def inorder(current):
            """
                this function print the tree starts from the current
                parameters:
                    current: the starts root point
            """
            # if arrive to the last of the sub tree stop the recursion
            if not current:
                return

            # call for left side
            inorder(current.left)

            # print the current node
            print(current.data, end="")

            # call for right side
            inorder(current.right)
        inorder(self.root)

    def sub_is_perfect(self, root, level=0):
        """
            this function check if the sub tree is prefect or not
            parameters:
                root: the root the sub tree
                level: the current level of the sub tree
            returns: the status of sub tree is perfect or not
        """
        # if the subtree is empty return true with current level
        if not root:
            return [True, level]
        
        # check for left side
        left_side = self.sub_is_perfect(root.left, level+1)
        
        # if the return of left side is false, return false with current level
        if not left_side[0]:
            return [False, left_side[1]]
        
        # check for right side
        right_side = self.sub_is_perfect(root.right, level+1)
        
        # check left and right for levels
        if right_side[0] and left_side[1] == right_side[1]:
            return [True, left_side[1]]
        
        # if arraive to this part, the sub tree is not perfect
        return [False, max(left_side[1], right_side[1])]
    
    def is_perfect(self):
        """
            this function check if the tree is prefect or not
            returns: the status of tree is perfect or not
        """
        return self.sub_is_perfect(self.root)[0]

    def _tree_height(self, root):
        """
            this function return the height of the sub tree
            parameters:
                root: the root you will start get the height from it
                height: the height of the subtree
            returns: the height of the sub tree
        """
        # if no root, return -1
        if not root:
            return -1
        
        # return the max of left and right
        return 1 + max(self._tree_height(root.left), self._tree_height(root.right))
    
    def tree_height(self):
        """
            this function return the height of the tree
            returns: the height of the tree
        """
        return self._tree_height(self.root)
    
    def _is_perfect_v2(self, root, height):
        """
            this function return the status of the tree is perfect of not insted of the height
            parameters:
                root: the root of the sub tree
                height: the height of current root
            return: the status of the tree is perfect or not
        """
        # if the current root is leaf, if the height is 0, this is perfect, not this is not perfect
        if not root.left and not root.right:
            return height == 0
        
        # check if the root have one child
        if (root.left and not root.right) or (root.right and not root.left):
            return False
        
        # return the status of left and right
        return self._is_perfect_v2(root.left, height-1) and self._is_perfect_v2(root.right, height-1)
    def is_perfect_v2(self):
        """
            this function return the status of the tree is perfect of not insted of the height
        """
        tree_height = self.tree_height()
        return self._is_perfect_v2(self.root, tree_height)
if __name__ == "__main__":
    # tree
    tree = BinaryTree(1)

    assert tree.is_perfect()
    assert tree.is_perfect_v2()

    tree.add([2], ['L'])
    assert not tree.is_perfect()
    assert not tree.is_perfect_v2()

    tree.add([3], ['R'])
    assert tree.is_perfect()
    assert tree.is_perfect_v2()

    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 15], ['R', 'R', 'L'])
    assert not tree.is_perfect()
    assert not tree.is_perfect_v2()

    tree.add([2, 5, 13], ['L', 'R', 'L'])
    tree.add([3, 6, 12], ['R', 'R', 'R'])
    tree.add([3, 14, 15], ['R', 'L', 'L'])
    tree.add([3, 14, 16], ['R', 'L', 'R'])
    assert tree.is_perfect()
    assert tree.is_perfect_v2()
    print(tree.length)
    
    
