class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.data)

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

    def first_not_perfect_check(self):
        """
            this function handle first check for the tree if no have any node or 1 node
            returns:
                true if the tree is not perfect
        """
        return self.length <= 1
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
    def _tree_nodes(self, current):
        """
            this function return the total number of nodes
            parameters:
                current: the current node
            returns: total number of tree nodes
        """
        # if no current return 0
        if not current:
            return 0
        
        return 1 + self._tree_nodes(current.left) + self._tree_nodes(current.right)
    def tree_nodes(self):
        """
            this function return the total number of nodes
            returns: total number of tree nodes
        """
        
        return self._tree_nodes(self.root)
    def _longest_line(self, root, height):
        """
            this function return the longest line list starts from root
            parameters:
                root: the root will start from it
                height: the target height
            returns:
                the list of longest line with his status
        """
        # if no element, return nothing
        if not root:
            return None, False
        
        # if this is a leaf, if main height is 0
        # return true with the starts list
        
        if not root.left and not root.right:
            # use () to return data with status in one piece
            return ([root], True) if height == 0 else (None, False)

        # get left data and his status
        left_data, left_status = self._longest_line(root.left, height-1)
        
        # check if the left has the longest line
        if left_status:
            left_data.append(root)
            return left_data, True
        
        # get right data and his status
        right_data, right_status = self._longest_line(root.right, height-1)
        
        # check if the right has the longest line
        if right_status:
            right_data.append(root)
            return right_data, True
        return None, False
    def longest_left_line(self):
        """
            this function return the longest line in the left of root
            returns:
                Left Tree boundary
        """
        # get tree height
        tree_height = self.tree_height()
        
        # get longest line
        longest_line, _ = self._longest_line(self.root.left, tree_height - 1)
        
        # append root to him
        longest_line.append(self.root)
        
        return longest_line
def print_tree(root):
    """
        this function the binary tree recursively
        parameters:
            root: the root will start print the left and right from it
    """
    # if the root is none, return none(stop recursive)
    if not root:
        return None

    # print the data
    print(root.data)

    # call the function for subtress
    print_tree(root.left)

    print_tree(root.right)


def print_expression(root):
    """
        this funciton print the binary as postfix
        parameters:
            root: the root will start print the left and right from it
    """
    # check if the root is operator
    if not str(root.data).isdigit():
        left_side = print_expression(root.left)
        right_side = print_expression(root.right)

        return f"{left_side}{right_side}{root.data}"

    # if the root is a number, just return the value
    return root.data


def print_expression_postfix(root):
    """
        this funciton print the binary as postfix
        parameters:
            root: the root will start print the left and right from it
    """
    # if not have a root, the parent is a number
    if not root:
        return
    print_expression_postfix(root.left)
    print_expression_postfix(root.right)

    print(root.data, end='')


if __name__ == "__main__":

    # tree
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ["L", "L", "L",])
    tree.add([2, 4, 8, 20], ["L", "L", "R", "R"])
    tree.add([2, 5, 9], ["L", "R", "R",])
    tree.add([3, 6, 10], ["R", "R", "L",])

    # tree.print_inorder()
    print(tree.longest_left_line())