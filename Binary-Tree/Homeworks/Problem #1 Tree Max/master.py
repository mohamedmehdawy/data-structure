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

    def tree_max(self):
        """
            this function get the max value of the whole tree and return it
            returns: the max value in the tree
        """
        def get_sub_max(root):
            """
                this function get the max value for the sub tree and return it
                parameters:
                    root: the root of the sub tree
                returns: the max value of the sub tree
            """
            # if the root is none, return none
            if not root:
                return None

            # get left side value
            left_value = (get_sub_max(
                root.left).data if root.left else None) or float('-inf')
            right_value = (get_sub_max(
                root.right).data if root.right else None) or float('-inf')

            # return max value
            if root.data >= left_value and root.data >= right_value:
                return root
            elif left_value >= root.data and left_value >= right_value:
                return root.left
            else:
                return root.right
        return get_sub_max(self.root).data

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

    tree = BinaryTree(2)
    tree.add([3], ["L"])
    tree.add([13, 8], ["R", "R"])
    tree.add([13, 7], ["R", "L"])

    print(tree.tree_max())

    tree2 = BinaryTree(1)
    tree2.add([2, 4, 7], ["L", "L", "L",])
    tree2.add([2, 4, 8], ["L", "L", "R",])
    tree2.add([2, 5, 9], ["L", "R", "R",])
    tree2.add([3, 6, 10], ["R", "R", "L",])
    print(tree2.tree_max())
