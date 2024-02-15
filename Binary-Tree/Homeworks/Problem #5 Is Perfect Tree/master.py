class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)

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

    @staticmethod
    def add_node(current, value, direction):
        """
            this function link the node insted of his direction
            parameters:
                current: the current node will linked with the target node
                value: the value of current or new node
                direction: the direction of the linked (left or right)
        """
        # if the direction is left
        if direction == "L":
            if not current.left:
                # create new node and link with current.left
                current.left = Node(value)
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

    def is_perfect(self):
        """
            this function check if the tree is prefect or not
            returns: the status of tree is perfect or not
        """
        pass
